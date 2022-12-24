#! /usr/bin/env python3

import argparse
import csv
import pathlib

from src import predictor, selector


def main(argv):
    workloads = []

    for file in pathlib.Path(argv.directory[0]).glob("**/*.csv"):
        # print(file)

        with open(file, newline="") as f:
            rows = csv.DictReader(f)

            workloads.append([row for row in rows])
    # print("")

    # print(workloads[0])
    # print("")

    cores = sorted(set([row["setup core"] for row in workloads[0]]))

    # print(cores)
    # print("")

    frequencies = []

    for core in cores:
        frequencies.append(sorted(set([int(row["frequency"]) for row in workloads[0] if row["setup core"] == core])))

    # print(frequencies)
    # print("")

    pmus = sorted(set([row["event"] for row in workloads[0]]))

    # print(pmus)
    # print("")

    for workload in workloads:
        for i in range(len(cores)):
            for j in range(len(frequencies[i])):
                for k in range(len(pmus)):
                    row = workload[i * len(workload) // len(cores) + j * len(pmus) + k]

                    row["count"] = int(row["count"].replace(',', ''))
                    row["time"] = float(row["time"].replace(',', ''))

    # print(workloads[0])
    # print("")

    getPerFreqError(workloads, cores, frequencies)
    getPerCoreError(workloads, cores, frequencies)


def getPerFreqError(workloads, cores, frequencies):
    data = selector.PerFreqSelector(workloads).select(6)

    for i in range(len(cores)):
        for j in range(len(frequencies[i])):
            print("cores: ", cores[i], "frequencies: ", frequencies[i][j])
            print("")

            predictor.Predictor().predict(data[i][j])
            print("")
        print("")


def getPerCoreError(workloads, cores, frequencies):
    data = selector.PerCoreSelector(workloads).select(6)

    for i in range(len(cores)):
        print("cores: ", cores[i])
        print("")

        predictor.Predictor().predict(data[i])
        print("")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    group = parser.add_argument_group()

    group.add_argument("-d", "--directory", nargs=1, type=str, help="profiled directory")

    argv = parser.parse_args()

    if not argv.directory:
        parser.error("Should have profiled directory!")

    main(argv)
