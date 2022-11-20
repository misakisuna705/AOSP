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

    dataset = selector.Selector().select(6)

    # for i in range(len(cores)):
    # for j in range(len(frequencies[i])):
    # print("cores: ", cores[i], "frequencies: ", frequencies[i][j])
    # print("")

    # for item in dataset[i][j]:
    # print(item)
    # print("")
    # print("")

    flag = 1

    for i in range(len(cores)):
        for j in range(len(frequencies[i])):
            if (flag):
                model.Model().train(dataset[i][j])

                flag = 0


if __name__ == "__main__":
    main()
