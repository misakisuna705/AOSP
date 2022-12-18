#! /usr/bin/env python3

import csv

from src import predictor, selector


def main():
    workload = []

    with open("dat/Dhrystone/dry.csv", newline="") as f:
        rows = csv.DictReader(f)

        workload = [row for row in rows]

    cores = sorted(set([row["setup core"] for row in workload]))

    frequencies = []

    for core in cores:
        frequencies.append(sorted(set([int(row["frequency"]) for row in workload if row["setup core"] == core])))

    # print(cores, frequencies)

    getPerFreqError(cores, frequencies)
    # getPerCoreError(cores, frequencies)


def getPerFreqError(cores, frequencies):
    dataset = selector.PerFreqSelector().select(6)

    for i in range(len(cores)):
        for j in range(len(frequencies[i])):
            predictor.Predictor().predict(dataset[i][j])


def getPerCoreError(cores, frequencies):
    dataset = selector.PerCoreSelector().select(6)

    flag = 1

    for i in range(len(cores)):
        if (flag):
            flag = 0


if __name__ == "__main__":
    main()
