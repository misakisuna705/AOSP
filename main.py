#! /usr/bin/env python3

import csv

from src import model, selector


def main():
    # selector = Selector()

    workload = []

    with open("bin/Dhrystone/dry.csv", newline="") as f:
        rows = csv.DictReader(f)

        workload = [row for row in rows]

    cores = sorted(set([row["setup core"] for row in workload]))

    frequencies = []

    for core in cores:
        frequencies.append(sorted(set([int(row["frequency"]) for row in workload if row["setup core"] == core])))

    # print(cores, frequencies)

    dataset = selector.Selector().select(6)

    # for i in range(len(cores)):
    # for j in range(len(frequencies[i])):
    # for pmu in dataset[i][j]:
    # print(pmu["pmu"])
    # print("")

    for i in range(len(cores)):
        for j in range(len(frequencies[i])):
            model.Model().train(dataset[i][j])


if __name__ == "__main__":
    main()
