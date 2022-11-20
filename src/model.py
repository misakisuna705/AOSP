#! /usr/bin/env python3

import tensorflow as tf


class Model(object):

    def __init__(self) -> None:
        pass

    def train(self, dataset):
        print(dataset)


def main():
    model = Model()

    model.train(6)


if __name__ == "__main__":
    main()
