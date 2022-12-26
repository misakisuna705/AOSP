#! /usr/bin/env python3

import logging

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

    perFreqFormatter.format()
    perCoreFormatter.format()


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
        dataColumns = [[{} for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                qualifiers = []
                meanTimes = []

                for k in range(len(self.pmus)):
                    counts = []

                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

                        meanTime = sum(workload["time"][anchor:anchor + len(self.pmus)]) / len(workload["time"][anchor:anchor + len(self.pmus)])

                        idx = anchor + k

                        qualifiers.append(workload["event"][idx]) if (workload["event"][idx] not in qualifiers) else None
                        counts.append(workload["count"][idx])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                    dataColumns[i][j] |= {qualifiers[k]: counts}

                dataColumns[i][j] |= {"times": meanTimes}

        # for i in range(len(self.cores)):
        # for j in range(len(self.frequencies[i])):
        # print("cores: ", self.cores[i], "frequencies: ", self.frequencies[i][j])
        # print("")

        # print(dataColumns[i][j])
        # print("")
        # print("")

        return [[pd.DataFrame(dataColumns[i][j]) for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]


class PerCoreFormatter(_Formatter):

    def __init__(self, workloads) -> None:
        super().__init__(workloads)

    def _format(self):
        dataColumns = [{} for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            qualifiers = []
            meanTimes = []

            for j in range(len(self.pmus)):
                counts = []

                for k in range(len(self.frequencies[i])):
                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + k * len(self.pmus)

                        meanTime = sum(workload["time"][anchor:anchor + len(self.pmus)]) / len(workload["time"][anchor:anchor + len(self.pmus)])

                        idx = anchor + j

                        qualifiers.append(workload["event"][idx]) if (workload["event"][idx] not in qualifiers) else None
                        counts.append(workload["count"][idx])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                dataColumns[i] |= {qualifiers[j]: counts}

            dataColumns[i] |= {"times": meanTimes}

        # for i in range(len(self.cores)):
        # print("cores: ", self.cores[i])
        # print("")

        # print(dataColumns[i])
        # print("")

        return [pd.DataFrame(dataColumns[i]) for i in range(len(self.cores))]


if __name__ == "__main__":

    main()
