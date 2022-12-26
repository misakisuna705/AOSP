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
        # print(dataframe, "\n")

        X, y = self._select(dataframe, 6)
        X_train, X_test, y_train, y_test = self._split(X, y, 0.8)
        model = self._train(X_train, y_train)
        self._test(X_test, y_test, model)

    def _select(self, dataframe, num):
        # selector = sklearn.feature_selection.RFE(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)
        # selector = sklearn.feature_selection.SelectFromModel(estimator=sklearn.linear_model.LinearRegression(), max_features=num)
        # selector = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=num)
        selector = sklearn.feature_selection.SequentialFeatureSelector(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)

        selector.fit_transform(dataframe.iloc[:, :-1], dataframe.iloc[:, -1])

        return dataframe.iloc[:, selector.get_support(indices=True)], dataframe.iloc[:, -1]

    def _split(self, X, y, ratio):
        return sklearn.model_selection.train_test_split(X, y, train_size=ratio, random_state=42)

    def _train(self, X_train, y_train):
        return self._trainedBySklearnLinearRegression(X_train, y_train)
        # return self._trainedByStatsmodelsOLS(X_train, y_train)

    def _trainedBySklearnLinearRegression(self, X_train, y_train):
        model = sklearn.linear_model.LinearRegression().fit(X_train, y_train)

        summary = pd.DataFrame(columns=X_train.columns)  # "coefficient weight

        summary.loc[len(summary.index)] = model.coef_.tolist()
        summary["intercept bias"] = model.intercept_
        summary["robustness R²"] = model.score(X_train, y_train)

        print(summary, "\n")

        return model

    def _trainedByStatsmodelsOLS(self, X_train, y_train):
        model = statsmodels.api.OLS(y_train, X_train).fit()

        print(model.summary(), "\n")

        return model

    def _test(self, X_test, y_test, model):
        y_pred = model.predict(X_test)

        # print(y_test.to_frame().assign(y_pred=y_pred), "\n")

        print(
            pd.DataFrame({
                "R²": [sklearn.metrics.r2_score(y_test, y_pred)],
                "Max error (s)": [sklearn.metrics.max_error(y_test, y_pred)],
                "Median absolute error (s)": [sklearn.metrics.median_absolute_error(y_test, y_pred)],
                "Mean absolute error (s)": [sklearn.metrics.mean_absolute_error(y_test, y_pred)],
                "Mean squared error (s²)": [sklearn.metrics.mean_squared_error(y_test, y_pred)],
                "Mean absolute percentage error (%)": [sklearn.metrics.mean_absolute_percentage_error(y_test, y_pred) * 100]
            }), "\n")


if __name__ == "__main__":
    main()
