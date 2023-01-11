#! /usr/bin/env python3

import logging
import math

# import matplotlib.pyplot
import numpy
import pandas as pd
# import scipy.cluster.hierarchy
import sklearn.cluster
import sklearn.feature_selection
import sklearn.linear_model
import sklearn.metrics
import sklearn.model_selection
import statsmodels.stats.outliers_influence

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

        # dataframe = self._filter(dataframe)  # filter
        X, y = self._select(dataframe, 6)  # selector

        for foldID, (trainIdxs, testIdxs) in enumerate(sklearn.model_selection.KFold(n_splits=5, shuffle=True, random_state=42).split(X)):  # spliter
            # print(trainIdxs.tolist())
            # print(testIdxs.tolist(), "\n")

            xTrain, xTest, yTrain, yTest = X.iloc[trainIdxs], X.iloc[testIdxs], y.iloc[trainIdxs], y.iloc[testIdxs]
            model = self._train(xTrain, yTrain)  # predictor
            result.append(pd.concat([pd.DataFrame({"fold": [foldID]}), self._test(xTest, yTest, model)], axis=1))

        return pd.concat(result, ignore_index=True)

    def _filter(self, dataframe):
        dups = [["raw-cpu-cycles", "raw-bus-cycles"], ["raw-inst-retired", "raw-inst-spec"], ["raw-br-retired", "raw-br-pred"],
                ["raw-br-mis-pred-retired", "raw-br-mis-pred"], ["raw-br-immed-retired", "raw-br-immed-spec"], ["raw-br-return-retired", "raw-br-return-spec"],
                ["raw-op-retired", "raw-op-spec"], ["raw-sve-inst-retired", "raw-sve-inst-spec"], ["raw-pc-write-retired", "raw-pc-write-spec"],
                ["raw-l1i-cache", "raw-l1i-tlb"], ["raw-l1d-cache", "raw-l1d-tlb"], ["raw-unaligned-ldst-retired", "raw-unaligned-ldst-spec"],
                ["raw-l1d-cache-rd", "raw-ld-retired", "raw-ld-spec"], ["raw-l1d-cache-wr", "raw-l1d-cache-allocate", "raw-st-retired", "raw-st-spec"],
                ["raw-l2d-cache-wr", "raw-l2d-cache-allocate", "raw-l1d-cache-wb"], ["raw-l3d-cache", "raw-ll-cache"],
                ["raw-l3d-cache-refill", "raw-ll-cache-miss"], ["raw-l3d-cache-rd", "raw-ll-cache-rd"], ["raw-l3d-cache-refill-rd", "raw-ll-cache-miss-rd"],
                ["raw-l3d-cache-wr", "raw-l3d-cache-allocate", "raw-l2d-cache-wb"], ["raw-mem-access-wr", "raw-l3d-cache-wb"]]

        for dup in dups:
            best = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression,
                                                         k=1).fit(dataframe[dup], dataframe.iloc[:, -1]).get_support(indices=True)

            keep = dataframe[dup].iloc[:, best].columns

            dataframe.drop(dataframe[dup].columns.difference(keep), axis=1, inplace=True)

        for col in dataframe.columns:
            dataframe.drop(col, axis=1, inplace=True) if (dataframe[col] == 0).all() else None

        # scipy.cluster.hierarchy.dendrogram(scipy.cluster.hierarchy.linkage(dataframe.iloc[:, :-1].T, method="ward"), labels=dataframe.iloc[:, :-1].columns)

        # matplotlib.pyplot.show()

        return dataframe

    def _select(self, dataframe, num):
        # selector = sklearn.feature_selection.RFE(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)
        # selector = sklearn.feature_selection.SelectFromModel(estimator=sklearn.linear_model.LinearRegression(), max_features=num)
        # selector = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=num)
        # selector = sklearn.feature_selection.SequentialFeatureSelector(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)
        # selector = sklearn.feature_selection.SelectKBest(score_func=self._evalWithClusteringBest, k=num)
        selector = sklearn.feature_selection.SelectKBest(score_func=self._evalWithWalker2016, k=num)

        selector.fit(dataframe.iloc[:, :-1], dataframe.iloc[:, -1])

        # print(
        # pd.DataFrame({
        # "ID": [item for item in selector.get_support(indices=True)],
        # "pmu": [dataframe.columns[item] for item in selector.get_support(indices=True)],
        # "group": [sklearn.cluster.FeatureAgglomeration(n_clusters=num).fit(dataframe.iloc[:, :-1]).labels_[item] for item in selector.get_support(indices=True)]
        # }), "\n")

        # return dataframe[["raw-cpu-cycles", "raw-inst-spec", "raw-l2d-cache-rd", "raw-unaligned-ldst-spec", "raw-dp-spec", "raw-l1i-cache",
        # "raw-bus-access"]], dataframe.iloc[:, -1]
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

    def _evalWithWalker2016(self, _X, y):
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
        # "pmu": ["X"] + ranks[0:9],
        # "VIF": [
        # statsmodels.stats.outliers_influence.variance_inflation_factor(statsmodels.tools.tools.add_constant(X[ranks[0:9]]).values, _)
        # for _ in range(len(statsmodels.tools.tools.add_constant(X[ranks[0:9]]).columns))
        # ]
        # }))

        weights = [int() for _ in range(len(X.columns))]

        for idx, item in enumerate(list((reversed(ranks)))):
            weights[item] = idx

        return numpy.array(weights)

    def _evalWithClusteringBest(self, _X, y):
        X = pd.DataFrame(_X)

        clusters = [[] for _ in range(6)]

        for idx, item in enumerate(sklearn.cluster.FeatureAgglomeration(n_clusters=6).fit(X).labels_):
            clusters[item].append(X.columns[idx])

        weights = [int() for _ in range(len(X.columns))]

        for cluster in clusters:
            best = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=1).fit(X[cluster], y).get_support(indices=True)

            weights[X.columns.get_loc(X[cluster].iloc[:, best].columns[0])] = 1

        return numpy.array(weights)


if __name__ == "__main__":
    main()
