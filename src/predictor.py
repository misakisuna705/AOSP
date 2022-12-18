#! /usr/bin/env python3

import pandas as pd
import sklearn.linear_model
import sklearn.metrics
import sklearn.model_selection
import tensorflow as tf


class Predictor(object):

    def __init__(self) -> None:
        pass

    def predict(self, data):
        dataframe = pd.DataFrame.from_dict(data)  # pd.read_csv

        # print(dataframe)
        # print("")

        self._predictRegression(dataframe)

    def _predictRegression(self, dataframe):
        self._regressBySklearn(dataframe)
        # self._regressByTensorflow(dataframe)

    def _regressBySklearn(self, dataframe):
        X = dataframe.iloc[:, :-1]
        y = dataframe.iloc[:, -1]

        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, train_size=0.8, random_state=0)

        regressor = sklearn.linear_model.LinearRegression()

        model = regressor.fit(X_train, y_train)

        print("coefficient weights: ", model.coef_.tolist())
        print("intercept bias: ", model.intercept_)
        print("robustness rsquare: ", model.score(X, y))
        print("")
        print("MAPE: ", sklearn.metrics.mean_absolute_percentage_error(y_test, regressor.predict(X_test)) * 100, "%")
        print("")

    def _regressByTensorflow(self, dataframe):
        dataset = tf.data.Dataset.from_tensor_slices((dataframe.iloc[:, :-1], dataframe.iloc[:, -1]))

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


def main():
    pass


if __name__ == "__main__":
    main()
