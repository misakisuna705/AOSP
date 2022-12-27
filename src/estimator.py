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

        for trainIdxs, testIdxs in sklearn.model_selection.KFold(n_splits=5, shuffle=True, random_state=42).split(X):
            # print(trainIdxs)
            # print(testIdxs)

            X_train, X_test, y_train, y_test = X.iloc[trainIdxs], X.iloc[testIdxs], y.iloc[trainIdxs], y.iloc[testIdxs]

            model = self._train(X_train, y_train)
            self._test(X_test, y_test, model)

    def _select(self, dataframe, num):
        # selector = sklearn.feature_selection.RFE(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)
        # selector = sklearn.feature_selection.SelectFromModel(estimator=sklearn.linear_model.LinearRegression(), max_features=num)
        # selector = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=num)
        selector = sklearn.feature_selection.SequentialFeatureSelector(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=num)

        selector.fit_transform(dataframe.iloc[:, :-1], dataframe.iloc[:, -1])

        return dataframe.iloc[:, selector.get_support(indices=True)], dataframe.iloc[:, -1]

    def _train(self, X_train, y_train):
        model = sklearn.linear_model.LinearRegression().fit(X_train, y_train)
        # model = sklearn.linear_model.Ridge(alpha=3.0).fit(X_train, y_train)

        summary = pd.DataFrame(columns=X_train.columns)  # "coefficient weight

        summary.loc[len(summary.index)] = model.coef_.tolist()
        summary["bias (intercept)"] = model.intercept_
        summary["robustness (R²)"] = model.score(X_train, y_train)

        # print(summary, "\n")

        return model

    def _test(self, X_test, y_test, model):
        y_pred = model.predict(X_test)

        # print(y_test.to_frame().assign(y_pred=y_pred), "\n")

        print(
            pd.DataFrame({
                # "R²": [sklearn.metrics.r2_score(y_test, y_pred)],
                "Mean absolute percentage error (%)": [sklearn.metrics.mean_absolute_percentage_error(y_test, y_pred) * 100],
                # "Mean absolute error (s)": [sklearn.metrics.mean_absolute_error(y_test, y_pred)],
                # "Max error (s)": [sklearn.metrics.max_error(y_test, y_pred)],
                # "Median absolute error (s)": [sklearn.metrics.median_absolute_error(y_test, y_pred)],
                # "Mean squared error (s²)": [sklearn.metrics.mean_squared_error(y_test, y_pred)],
                # "Mean squared log error (s²)": [sklearn.metrics.mean_squared_log_error(y_test, y_pred)],
            }),
            "\n")


if __name__ == "__main__":
    main()
