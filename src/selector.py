#! /usr/bin/env python3

import logging
import statistics

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s line:%(lineno)-3d %(levelname)-8s ] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)


def main():
    perFreqSelector = PerFreqSelector()
    perCoreSelector = PerCoreSelector()

    perFreqSelector.select(6)
    perCoreSelector.select(6)


class _Selector(object):

    def __init__(self, workloads) -> None:

        self.workloads = workloads

        # print(self.workloads)

        self.cores = sorted(set(workloads[0]["setup core"]))

        # print(self.cores)

        self.frequencies = []

        for anchor in range(len(self.cores)):
            step = len(workloads[0]) // len(self.cores)

            self.frequencies.append(sorted(set(workloads[0]["frequency"][anchor * step:anchor * step + step])))

        # print(self.frequencies)

        self.pmus = sorted(set(workloads[0]["event"][0:len(workloads[0]) // len(self.cores) // len(self.frequencies[0])]))

        # print(self.pmus)

    def select(self, num):
        ranks = self._rank()
        dataframes = self._format(ranks, num)

        return dataframes


class PerFreqSelector(_Selector):

    def __init__(self, workloads) -> None:
        super().__init__(workloads)

    def _rank(self):
        ranks = [[[{"pmu": (), "samples": [], "correlation": 0.0} for k in range(len(self.pmus))] for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for workload in self.workloads:
            for i in range(len(self.cores)):
                for j in range(len(self.frequencies[i])):
                    for k in range(len(self.pmus)):
                        idx = i * len(workload) // len(self.cores) + j * len(self.pmus) + k

                        ranks[i][j][k]["pmu"] = (k, self.pmus[k])
                        ranks[i][j][k]["samples"].append((workload["count"][idx], workload["time"][idx]))

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                for k in range(len(self.pmus)):
                    count = [sample[0] for sample in ranks[i][j][k]["samples"]]
                    time = [sample[1] for sample in ranks[i][j][k]["samples"]]

                    ranks[i][j][k]["correlation"] = pow(statistics.correlation(count, time), 2) if statistics.stdev(count) and statistics.stdev(time) else False

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                ranks[i][j] = sorted(ranks[i][j], key=lambda dict: dict["correlation"], reverse=True)

        # logging.info("correlation ranks: ")
        # for i in range(len(self.cores)):
        # for j in range(len(self.frequencies[i])):
        # for k in range(len(self.pmus)):
        # logging.info("\tcore" + str(self.cores[i]) + " frequency: " + str(self.frequencies[i][j]).ljust(8, " ") + "No." +
        # str(ranks[i][j][k]["pmu"][0]).ljust(3, " ") + " " + ranks[i][j][k]["pmu"][1].ljust(27, " ") + str(ranks[i][j][k]["correlation"]))
        # logging.info("")

        return ranks

    def _format(self, ranks, num):
        datalist = [[[] for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                qualifiers = []
                meanTimes = []

                for k in range(num):
                    counts = []

                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

                        meanTime = statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])

                        idx = anchor + ranks[i][j][k]["pmu"][0]

                        qualifiers.append(workload["event"][idx]) if (workload["event"][idx] not in qualifiers) else None
                        counts.append(workload["count"][idx])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                    datalist[i][j].append({qualifiers[k]: counts})

                datalist[i][j].append({"times": meanTimes})

        # for i in range(len(self.cores)):
        # for j in range(len(self.frequencies[i])):
        # print("cores: ", self.cores[i], "frequencies: ", self.frequencies[i][j])
        # print("")

        # for item in datalist[i][j]:
        # print(item)
        # print("")
        # print("")
        # print("")

        datadict = [[{} for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                for item in datalist[i][j]:
                    datadict[i][j] |= item

        dataframes = [[pd.DataFrame() for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                dataframes[i][j] = pd.DataFrame.from_dict(datadict[i][j])

        # for i in range(len(self.cores)):
        # for j in range(len(self.frequencies[i])):
        # print("cores: ", self.cores[i], "frequencies: ", self.frequencies[i][j])
        # print("")

        # print(dataframes[i][j])
        # print("")
        # print("")

        return dataframes


class PerCoreSelector(_Selector):

    def __init__(self, workloads) -> None:
        super().__init__(workloads)

    def _rank(self):
        ranks = [[{"pmu": (), "samples": [], "correlation": 0.0} for j in range(len(self.pmus))] for i in range(len(self.cores))]

        for workload in self.workloads:
            for i in range(len(self.cores)):
                for j in range(len(self.pmus)):
                    ranks[i][j]["pmu"] = (j, self.pmus[j])

                    for k in range(len(self.frequencies[i])):
                        idx = i * len(workload) // len(self.cores) + k * len(self.pmus) + j

                        ranks[i][j]["samples"].append((workload["count"][idx], workload["time"][idx]))

        for i in range(len(self.cores)):
            for j in range(len(self.pmus)):
                count = [sample[0] for sample in ranks[i][j]["samples"]]
                time = [sample[1] for sample in ranks[i][j]["samples"]]

                ranks[i][j]["correlation"] = pow(statistics.correlation(count, time), 2) if statistics.stdev(count) and statistics.stdev(time) else False

        for i in range(len(self.cores)):
            ranks[i] = sorted(ranks[i], key=lambda dict: dict["correlation"], reverse=True)

        # logging.info("correlation ranks: ")
        # for i in range(len(self.cores)):
        # for j in range(len(self.pmus)):
        # logging.info("\tcore" + str(self.cores[i]) + " No." + str(ranks[i][j]["pmu"][0]).ljust(3, " ") + " " + ranks[i][j]["pmu"][1].ljust(27, " ") +
        # str(ranks[i][j]["correlation"]))
        # logging.info("")

        return ranks

    def _format(self, ranks, num):
        datalist = [[] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            qualifiers = []
            meanTimes = []

            for j in range(num):
                counts = []

                for k in range(len(self.frequencies[i])):
                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + k * len(self.pmus)

                        meanTime = statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])

                        idx = anchor + ranks[i][j]["pmu"][0]

                        qualifiers.append(workload["event"][idx]) if (workload["event"][idx] not in qualifiers) else None
                        counts.append(workload["count"][idx])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                datalist[i].append({qualifiers[j]: counts})

            datalist[i].append({"times": meanTimes})

        # for i in range(len(self.cores)):
        # print("cores: ", self.cores[i])
        # print("")

        # for item in datalist[i]:
        # print(item)
        # print("")
        # print("")

        datadict = [{} for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            for item in datalist[i]:
                datadict[i] |= item

        dataframes = [pd.DataFrame() for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            dataframes[i] = pd.DataFrame.from_dict(datadict[i])

        # for i in range(len(self.cores)):
        # print("cores: ", self.cores[i])
        # print("")

        # print(dataframes[i])
        # print("")

        return dataframes


if __name__ == "__main__":

    main()
