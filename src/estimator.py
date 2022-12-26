#! /usr/bin/env python3

import logging

import sklearn.feature_selection
import sklearn.linear_model
import sklearn.metrics
import sklearn.model_selection
import statsmodels.api

# import tensorflow as tf

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

        X, y = self._select(dataframe)

        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, train_size=0.8, random_state=42)

        self._predict(X_train, X_test, y_train, y_test)

    def _select(self, dataframe):
        # selector = sklearn.feature_selection.RFE(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=6)
        # selector = sklearn.feature_selection.SelectFromModel(estimator=sklearn.linear_model.LinearRegression(), max_features=6)
        # selector = sklearn.feature_selection.SelectKBest(score_func=sklearn.feature_selection.r_regression, k=6)
        selector = sklearn.feature_selection.SequentialFeatureSelector(estimator=sklearn.linear_model.LinearRegression(), n_features_to_select=6)

        selector.fit_transform(dataframe.iloc[:, :-1], dataframe.iloc[:, -1])

        # print(list(dataframe.iloc[:, selector.get_support(indices=True)].columns))
        # print("")

        return dataframe.iloc[:, selector.get_support(indices=True)], dataframe.iloc[:, -1]

    def _predict(self, X_train, X_test, y_train, y_test):
        self._predictedBySklearnLinearRegression(X_train, X_test, y_train, y_test)
        # self._predictedByStatsmodelsOLS(X_train, X_test, y_train, y_test)
        # self._regressByTensorflow(X_train, X_test, y_train, y_test)

    def _predictedBySklearnLinearRegression(self, X_train, X_test, y_train, y_test):
        model = sklearn.linear_model.LinearRegression().fit(X_train, y_train)

        print("Sklearn LinearRegression: ")
        # print("coefficient weights: ", model.coef_.tolist())
        # print("intercept bias: ", model.intercept_)
        # print("robustness R²: ", model.score(X, y))
        # print("")

        y_pred = model.predict(X_test)

        # print(y_test.to_frame().assign(y_pred=y_pred))
        # print("")

        # print("R²: ", sklearn.metrics.r2_score(y_test, y_pred))
        # print("")
        # print("Max error: ", sklearn.metrics.max_error(y_test, y_pred), "(s)")
        # print("Median absolute error: ", sklearn.metrics.median_absolute_error(y_test, y_pred), "(s)")
        # print("Mean absolute error: ", sklearn.metrics.mean_absolute_error(y_test, y_pred), "(s)")
        # print("Mean squared error: ", sklearn.metrics.mean_squared_error(y_test, y_pred), "(s²)")
        # print("")
        print("Mean absolute percentage error: ", sklearn.metrics.mean_absolute_percentage_error(y_test, y_pred) * 100, "(%)")
        print("")

    def _predictedByStatsmodelsOLS(self, X_train, X_test, y_train, y_test):
        model = statsmodels.api.OLS(y_train, X_train).fit()

        print("Statsmodels OLS: ")
        # print(model.summary())
        # print("")

        y_pred = model.predict(X_test)

        # print(y_test.to_frame().assign(y_pred=y_pred))
        # print("")

        print("Mean absolute percentage error: ", sklearn.metrics.mean_absolute_percentage_error(y_test, y_pred) * 100, "(%)")
        print("")

    def _regressByTensorflow(self, dataframe):
        # dataset = tf.data.Dataset.from_tensor_slices((dataframe.iloc[:, :-1], dataframe.iloc[:, -1]))

        # print("")
        # print(dataset)
        # print("")

        # for features, target in dataset:
        # print(features, target)
        # print("")

        # for data in dataset:
        # print(data)
        # print("")

        # def _split(dataset):
        # dataset = dataset.shuffle(len(dataset))

        # trainSize = int(0.8 * len(dataset))
        # validationSize = int(0.1 * len(dataset))

        # trainSet = dataset.take(trainSize)
        # validationSet = dataset.skip(trainSize).take(validationSize)
        # testSet = dataset.skip(trainSize).skip(validationSize)

        # return trainSet, validationSet, testSet

        # trainSet, validationSet, testSet = _split(dataset)

        # trainSet = trainSet.shuffle(len(trainSet)).batch(4)

        # model = tf.keras.Sequential([tf.keras.layers.Normalization(axis=None)])

        # model.compile(loss=tf.losses.MeanSquaredError(), optimizer=tf.keras.optimizers.SGD(learning_rate=0.01))

        # model.fit(trainSet, epochs=100)

        # loss, accuracy = model.evaluate(validationSet)

        # print(loss, accuracy)

        pass


if __name__ == "__main__":
    main()
