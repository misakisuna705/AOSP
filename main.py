#! /usr/bin/env python3

import argparse
import logging
import pathlib

import pandas as pd

from src import estimator, formatter, preprocessor

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s line:%(lineno)-3d %(levelname)-8s ] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)


def main(argv):
    workloads = [pd.read_csv(file) for file in pathlib.Path(argv.directory[0]).glob("**/*.csv")]

    # print(workloads)
    # print("")

    cores = sorted(set(workloads[0]["setup core"]))

    # print(cores)
    # print("")

    frequencies = []

    for anchor in range(len(cores)):
        step = len(workloads[0]) // len(cores)

        frequencies.append(sorted(set(workloads[0]["frequency"][anchor * step:anchor * step + step])))

    # print(frequencies)
    # print("")

    pmus = sorted(set(workloads[0]["event"][0:len(workloads[0]) // len(cores) // len(frequencies[0])]))

    # print(pmus)
    # print("")

    for workload in workloads:
        for i in range(len(cores)):
            for j in range(len(frequencies[i])):
                for k in range(len(pmus)):
                    idx = i * len(workload) // len(cores) + j * len(pmus) + k

                    workload.loc[idx, "count"] = int(workload["count"][idx].replace(",", ""))
                    workload.loc[idx, "time"] = float(workload["time"][idx])

    # print(workloads)
    # print("")

    workloads = preprocessor.Preprocessor(workloads).preprocess()

    # print(workloads)
    # print("")

    getPerFreqError(workloads, cores, frequencies)
    getPerCoreError(workloads, cores, frequencies)


def getPerFreqError(workloads, cores, frequencies):
    dataframes = formatter.PerFreqFormatter(workloads).format()

    print("getPerFreqError: \n")
    for i in range(len(cores)):
        for j in range(len(frequencies[i])):
            result = estimator.Estimator().estimate(dataframes[i][j])

            print(pd.concat([pd.DataFrame({"core": [cores[i] for _ in range(len(result))], "frequency": [frequencies[i][j] for _ in range(len(result))]}), result], axis=1))


def getPerCoreError(workloads, cores, frequencies):
    dataframes = formatter.PerCoreFormatter(workloads).format()

    print("getPerCoreError: \n")
    for i in range(len(cores)):
        result = estimator.Estimator().estimate(dataframes[i])

        print(pd.concat([pd.DataFrame({"core": [cores[i] for _ in range(len(result))], "frequency": ["*********" for _ in range(len(result))]}), result], axis=1))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    group = parser.add_argument_group()

    group.add_argument("-d", "--directory", nargs=1, type=str, help="profiled directory")

    argv = parser.parse_args()

    if not argv.directory:
        parser.error("Should have profiled directory!")

    main(argv)
