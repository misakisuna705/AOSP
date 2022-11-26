#! /usr/bin/env python3

import tensorflow as tf


class Predictor(object):

    def __init__(self) -> None:
        pass

    def train(self, dataset):
        for item in dataset:
            print(item)
            print("")
        print("")


def main():
    predictor = Predictor()

    predictor.train()


if __name__ == "__main__":
    main()
