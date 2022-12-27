#! /usr/bin/env python3

import logging

import pandas as pd
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

        X, y = self._select(dataframe, 6)

        result = []

        for foldID, (trainIdxs, testIdxs) in enumerate(sklearn.model_selection.KFold(n_splits=5, shuffle=True, random_state=42).split(X)):
            # print(trainIdxs.tolist())
            # print(testIdxs.tolist(), "\n")

            xTrain, xTest, yTrain, yTest = X.iloc[trainIdxs], X.iloc[testIdxs], y.iloc[trainIdxs], y.iloc[testIdxs]
            model = self._train(xTrain, yTrain)

            result.append(self._test(xTest, yTest, model, foldID))

        return pd.concat(result, axis=0)

    def _select(self, dataframe, num):
        # selector = sklearn.feature_selection.RFE(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)
        # selector = sklearn.feature_selection.SelectFromModel(estimator=sklearn.linear_model.LinearRegression(), max_features=num)
        selector = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=num)
        # selector = sklearn.feature_selection.SequentialFeatureSelector(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)

        selector.fit_transform(dataframe.iloc[:, :-1], dataframe.iloc[:, -1])

        return dataframe.iloc[:, selector.get_support(indices=True)], dataframe.iloc[:, -1]

    def _train(self, xTrain, yTrain):
        # model = sklearn.linear_model.Ridge(alpha=3.0).fit(xTrain, yTrain)
        model = sklearn.linear_model.LinearRegression().fit(xTrain, yTrain)

        summary = pd.DataFrame(columns=xTrain.columns)  # "coefficient weight

        summary.loc[len(summary.index)] = model.coef_.tolist()
        summary["bias (intercept)"] = model.intercept_
        summary["robustness (R²)"] = model.score(xTrain, yTrain)

        # print(summary, "\n")

        return model

    def _test(self, xTest, yTest, model, foldID):
        y_pred = model.predict(xTest)

        # print(yTest.to_frame().assign(y_pred=y_pred), "\n")

        return pd.DataFrame({
            "fold": [foldID],
            "R²": [sklearn.metrics.r2_score(yTest, y_pred)],
            "Mean absolute percentage error (%)": [sklearn.metrics.mean_absolute_percentage_error(yTest, y_pred) * 100],
            "Mean absolute error (s)": [sklearn.metrics.mean_absolute_error(yTest, y_pred)],
            "Max error (s)": [sklearn.metrics.max_error(yTest, y_pred)],
            "Median absolute error (s)": [sklearn.metrics.median_absolute_error(yTest, y_pred)],
            "Mean squared error (s²)": [sklearn.metrics.mean_squared_error(yTest, y_pred)],
        })


if __name__ == "__main__":
    main()
