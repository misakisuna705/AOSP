#! /usr/bin/env python3

# import matplotlib.pyplot

import logging

import pandas as pd
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


class Predictor(object):

    def __init__(self) -> None:
        pass

    def predict(self, dataframe):
        # print(dataframe)
        # print("")

        # self._predictRegression(dataframe)

        self._predictedByStatsmodelsOLS(dataframe)
        # self._predictedBySklearnLinearRegression(dataframe)
        # self._regressByTensorflow(dataframe)

    def _predictedByStatsmodelsOLS(self, dataframe):
        X = statsmodels.api.add_constant(dataframe.iloc[:, :-1])
        y = dataframe.iloc[:, -1]

        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, train_size=0.8, random_state=42)

        model = statsmodels.api.OLS(y_train, X_train).fit()

        print("predicted by Statsmodels OLS: ")
        print("")
        # print(model.summary())
        # print("")

        y_pred = model.predict(X_test)

        # print(y_test.to_frame().assign(y_pred=y_pred))
        # print("")

        print("Mean absolute percentage error: ", sklearn.metrics.mean_absolute_percentage_error(y_test, y_pred) * 100, "(%)")
        print("")

    def _predictedBySklearnLinearRegression(self, dataframe):
        X = dataframe.iloc[:, :-1]
        y = dataframe.iloc[:, -1]

        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, train_size=0.8, random_state=42)

        model = sklearn.linear_model.LinearRegression().fit(X_train, y_train)

        print("predicted by Sklearn LinearRegression: ")
        print("")
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
