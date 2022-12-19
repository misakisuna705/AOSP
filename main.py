#! /usr/bin/env python3

import csv

from src import predictor, selector


def main():
    workload = []

    # with open("dat/Weichun/Mibench/bitcnts/84600000.csv") as f:
    # with open("dat/Essen/MiBench/bitcount/bitcnt86400000_4XL.csv", newline="") as f:
    # with open("dat/Peihsuan/MiBench/bitcnts/84600000.csv", newline="") as f:
    with open("dat/Doshin/MiBench/bitcnts/84600000.csv", newline="") as f:

        rows = csv.DictReader(f)

        workload = [row for row in rows]

    cores = sorted(set([row["setup core"] for row in workload]))

    frequencies = []

    for core in cores:
        frequencies.append(sorted(set([int(row["frequency"]) for row in workload if row["setup core"] == core])))

    # print(cores, frequencies)

    getPerFreqError(cores, frequencies)
    getPerCoreError(cores, frequencies)


def getPerFreqError(cores, frequencies):
    data = selector.PerFreqSelector().select(6)

    for i in range(len(cores)):
        for j in range(len(frequencies[i])):
            print("cores: ", cores[i], "frequencies: ", frequencies[i][j])
            print("")

            predictor.Predictor().predict(data[i][j])
            print("")
        print("")


def getPerCoreError(cores, frequencies):
    data = selector.PerCoreSelector().select(6)

    for i in range(len(cores)):
        print("cores: ", cores[i])
        print("")

        predictor.Predictor().predict(data[i])
        print("")


if __name__ == "__main__":
    main()
