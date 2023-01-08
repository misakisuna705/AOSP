#! /usr/bin/env python3

import logging
import math
import sys

import matplotlib.pyplot
import numpy
import pandas as pd
import scipy.cluster.hierarchy
import sklearn.cluster
import sklearn.feature_selection
import sklearn.linear_model
import sklearn.metrics
import sklearn.model_selection

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s line:%(lineno)-3d %(levelname)-8s ] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)


def main():
    pass


class Estimator(object):

    def __init__(self) -> None:
        pass

    def estimate(self, dataframe):
        # print(dataframe, "\n")

        result = []

        dataframe = self._filter(dataframe)  # filter
        X, y = self._select(dataframe, 6)  # selector

        for foldID, (trainIdxs, testIdxs) in enumerate(sklearn.model_selection.KFold(n_splits=5, shuffle=True, random_state=42).split(X)):  # spliter
            # print(trainIdxs.tolist())
            # print(testIdxs.tolist(), "\n")

            xTrain, xTest, yTrain, yTest = X.iloc[trainIdxs], X.iloc[testIdxs], y.iloc[trainIdxs], y.iloc[testIdxs]
            model = self._train(xTrain, yTrain)  # predictor
            result.append(pd.concat([pd.DataFrame({"fold": [foldID]}), self._test(xTest, yTest, model)], axis=1))

        return pd.concat(result, ignore_index=True)

    def _filter(self, dataframe):
        print(dataframe[["raw-l3d-cache", "raw-ll-cache"]], "\n")

        return dataframe

    def _select(self, dataframe, num):

        def _evalWithWalker2016(_X, y):
            X = pd.DataFrame(_X)

            ranks = list(range(len(X.columns)))

            for i in range(len(ranks)):
                if not i:
                    initEvent = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=1).fit(X, y).get_support(indices=True)[0]

                    ranks[i], ranks[initEvent] = ranks[initEvent], ranks[i]
                else:
                    bestEvent, bestR2 = i, -math.inf

                    for pmuEvent in range(i, len(ranks)):
                        selectedList = X.iloc[:, ranks[0:i] + [ranks[pmuEvent]]]

                        newR2 = sklearn.linear_model.LinearRegression().fit(selectedList, y).score(selectedList, y)

                        if (newR2 > bestR2):
                            bestEvent, bestR2 = pmuEvent, newR2

                    ranks[i], ranks[bestEvent] = ranks[bestEvent], ranks[i]

            # print(
            # pd.DataFrame({
            # "pmu": ["X"] + ranks[0:num],
            # "VIF": [
            # statsmodels.stats.outliers_influence.variance_inflation_factor(statsmodels.tools.tools.add_constant(dataframe[ranks[0:num]]).values, _)
            # for _ in range(len(statsmodels.tools.tools.add_constant(dataframe[ranks[0:num]]).columns))
            # ]
            # }))

            weights = [int() for _ in range(len(X.columns))]

            for idx, item in enumerate(list((reversed(ranks)))):
                weights[item] = idx

            return numpy.array(weights)

        # selector = sklearn.feature_selection.RFE(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)
        # selector = sklearn.feature_selection.SelectFromModel(estimator=sklearn.linear_model.LinearRegression(), max_features=num)
        # selector = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=num)
        # selector = sklearn.feature_selection.SequentialFeatureSelector(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)
        selector = sklearn.feature_selection.SelectKBest(score_func=_evalWithWalker2016, k=num)

        selector.fit(dataframe.iloc[:, :-1], dataframe.iloc[:, -1])

        # print(
        # pd.DataFrame({
        # "ID": [item for item in selector.get_support(indices=True)],
        # "pmu": [dataframe.columns[item] for item in selector.get_support(indices=True)],
        # "group": [sklearn.cluster.FeatureAgglomeration(n_clusters=num).fit(dataframe.iloc[:, :-1]).labels_[item] for item in selector.get_support(indices=True)]
        # }), "\n")

        return dataframe.iloc[:, selector.get_support(indices=True)], dataframe.iloc[:, -1]

    def _train(self, xTrain, yTrain):
        model = sklearn.linear_model.LinearRegression().fit(xTrain, yTrain)

        summary = pd.DataFrame(columns=xTrain.columns)  # "coefficient weight

        summary.loc[len(summary.index)] = model.coef_.tolist()
        summary["bias (intercept)"] = model.intercept_
        summary["robustness (R²)"] = model.score(xTrain, yTrain)

        # print(summary, "\n")

        return model

    def _test(self, xTest, yTest, model):
        y_pred = model.predict(xTest)

        # print(yTest.to_frame().assign(y_pred=y_pred), "\n")

        return pd.DataFrame({
            "R²": [sklearn.metrics.r2_score(yTest, y_pred)],
            "Mean absolute percentage error (%)": [sklearn.metrics.mean_absolute_percentage_error(yTest, y_pred) * 100],
            "Mean absolute error (s)": [sklearn.metrics.mean_absolute_error(yTest, y_pred)],
            "Max error (s)": [sklearn.metrics.max_error(yTest, y_pred)],
            "Median absolute error (s)": [sklearn.metrics.median_absolute_error(yTest, y_pred)],
            "Mean squared error (s²)": [sklearn.metrics.mean_squared_error(yTest, y_pred)],
        })


if __name__ == "__main__":
    main()
