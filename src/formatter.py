#! /usr/bin/env python3

import logging
import statistics

import pandas as pd

# import statsmodels.api
# import statsmodels.stats.outliers_influence

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s line:%(lineno)-3d %(levelname)-8s ] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)


def main():
    perFreqFormatter = PerFreqFormatter()
    perCoreFormatter = PerCoreFormatter()

    perFreqFormatter.format(6)
    perCoreFormatter.format(6)


class _Formatter(object):

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

    def format(self):
        dataframes = self._format()

        return dataframes


class PerFreqFormatter(_Formatter):

    def __init__(self, workloads) -> None:
        super().__init__(workloads)

    def _format(self):
        datadict = [[{} for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                qualifiers = []
                meanTimes = []

                for k in range(len(self.pmus)):
                    counts = []

                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

                        meanTime = statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])

                        idx = anchor + k

                        qualifiers.append(workload["event"][idx]) if (workload["event"][idx] not in qualifiers) else None
                        counts.append(workload["count"][idx])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                    datadict[i][j] |= {qualifiers[k]: counts}

                datadict[i][j] |= {"times": meanTimes}

        # for i in range(len(self.cores)):
        # for j in range(len(self.frequencies[i])):
        # print("cores: ", self.cores[i], "frequencies: ", self.frequencies[i][j])
        # print("")

        # print(datadict[i][j])
        # print("")
        # print("")

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


class PerCoreFormatter(_Formatter):

    def __init__(self, workloads) -> None:
        super().__init__(workloads)

    def _format(self):
        datadict = [{} for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            qualifiers = []
            meanTimes = []

            for j in range(len(self.pmus)):
                counts = []

                for k in range(len(self.frequencies[i])):
                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + k * len(self.pmus)

                        meanTime = statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])

                        idx = anchor + j

                        qualifiers.append(workload["event"][idx]) if (workload["event"][idx] not in qualifiers) else None
                        counts.append(workload["count"][idx])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                datadict[i] |= {qualifiers[j]: counts}

            datadict[i] |= {"times": meanTimes}

        # for i in range(len(self.cores)):
        # print("cores: ", self.cores[i])
        # print("")

        # print(datadict[i])
        # print("")

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
