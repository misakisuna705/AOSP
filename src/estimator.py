#! /usr/bin/env python3

import logging

import pandas as pd
import sklearn.feature_selection
import sklearn.linear_model
import sklearn.metrics
import sklearn.model_selection
import statsmodels.api

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
        # print(dataframe)
        # print("")

        X, y = self._select(dataframe, 6)

        X_train, X_test, y_train, y_test = self._split(X, y, 0.8)

        y_pred = self._predict(X_train, X_test, y_train, y_test)

        self._report(y_test, y_pred)

    def _select(self, dataframe, num):
        # selector = sklearn.feature_selection.RFE(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)
        # selector = sklearn.feature_selection.SelectFromModel(estimator=sklearn.linear_model.LinearRegression(), max_features=num)
        # selector = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=num)
        selector = sklearn.feature_selection.SequentialFeatureSelector(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)

        selector.fit_transform(dataframe.iloc[:, :-1], dataframe.iloc[:, -1])

        # print(list(dataframe.iloc[:, selector.get_support(indices=True)].columns))
        # print("")

        return dataframe.iloc[:, selector.get_support(indices=True)], dataframe.iloc[:, -1]

    def _split(self, X, y, ratio):
        return sklearn.model_selection.train_test_split(X, y, train_size=ratio, random_state=42)

    def _predict(self, X_train, X_test, y_train, y_test):
        return self._predictedBySklearnLinearRegression(X_train, X_test, y_train, y_test)
        # return self._predictedByStatsmodelsOLS(X_train, X_test, y_train, y_test)

    def _predictedBySklearnLinearRegression(self, X_train, X_test, y_train, y_test):
        model = sklearn.linear_model.LinearRegression().fit(X_train, y_train)

        print("coefficient weights: ", model.coef_.tolist())
        # print("intercept bias: ", model.intercept_)
        # print("robustness R²: ", model.score(X_train, y_train))
        print("")

        return model.predict(X_test)

    def _predictedByStatsmodelsOLS(self, X_train, X_test, y_train, y_test):
        model = statsmodels.api.OLS(y_train, X_train).fit()

        # print(model.summary())
        # print("")

        return model.predict(X_test)

    def _report(self, y_test, y_pred):
        print(y_test.to_frame().assign(y_pred=y_pred))
        print("")

        print(
            pd.DataFrame({
                "Sklearn": ["LinearRegression"],
                "R²": [sklearn.metrics.r2_score(y_test, y_pred)],
                "Max error (s)": [sklearn.metrics.max_error(y_test, y_pred)],
                "Median absolute error (s)": [sklearn.metrics.median_absolute_error(y_test, y_pred)],
                "Mean absolute error (s)": [sklearn.metrics.mean_absolute_error(y_test, y_pred)],
                "Mean squared error (s²)": [sklearn.metrics.mean_squared_error(y_test, y_pred)],
                "Mean absolute percentage error (%)": [sklearn.metrics.mean_absolute_percentage_error(y_test, y_pred) * 100]
            }))
        print("")


if __name__ == "__main__":
    main()
