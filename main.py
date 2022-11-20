#! /usr/bin/env python3

import csv

from src import model, selector


def main():
    workload = []

    with open("bin/Dhrystone/dry.csv", newline="") as f:
        rows = csv.DictReader(f)

        workload = [row for row in rows]

    cores = sorted(set([row["setup core"] for row in workload]))

    frequencies = []

    for core in cores:
        frequencies.append(sorted(set([int(row["frequency"]) for row in workload if row["setup core"] == core])))

    # print(cores, frequencies)

    worklists = selector.Selector().select(6)

    for worklist in worklists:
        for row in worklist:
            print(row)
        print("")

    flag = 1

    for i in range(len(cores)):
        for j in range(len(frequencies[i])):
            if (flag):
                # dataset = [sample for data in worklist[i][j] for sample in data["samples"]]

                # model.Model().train(dataset)

                flag = 0


if __name__ == "__main__":
    main()
