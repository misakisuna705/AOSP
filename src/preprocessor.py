#! /usr/bin/env python3

import statistics


def main(argv):
    pass


class Preprocessor(object):

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

    def preprocess(self):
        self._filter()

        return self._classify()

    def _filter(self):
        self.workloads = list(filter(self._isTimeOrdered, self.workloads))  # ##################################################################

        # for idx, workload in enumerate(self.workloads):
        # for i in range(len(self.cores)):
        # meanTimes = []

        # for j in range(len(self.frequencies[i])):
        # anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

        # meanTimes.append(int(statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])))

        # print("cores: ", self.cores[i], "meanTimes: ", meanTimes)
        # print("")

        # self.workloads = list(filter(self._isTimeStrictlyOrdered, self.workloads))  # ##################################################################

        # for idx, workload in enumerate(self.workloads):
        # for i in range(len(self.cores)):
        # meanTimes = []

        # for j in range(len(self.frequencies[i])):
        # anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

        # meanTimes.append(int(statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])))

        # print("cores: ", self.cores[i], "meanTimes: ", meanTimes)
        # print("")

        self.workloads = list(filter(self._isTimeLarge, self.workloads))  # ##################################################################

        # for idx, workload in enumerate(self.workloads):
        # for i in range(len(self.cores)):
        # meanTimes = []

        # for j in range(len(self.frequencies[i])):
        # anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

        # meanTimes.append(int(statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])))

        # print("cores: ", self.cores[i], "meanTimes: ", meanTimes)
        # print("")

    def _isTimeOrdered(self, workload):
        isOrdered = True

        for i in range(len(self.cores)):
            meanTimes = []

            for j in range(len(self.frequencies[i])):
                anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

                meanTimes.append(int(statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])))

            isOrdered &= meanTimes == sorted(meanTimes, reverse=True)

        return isOrdered

    def _isTimeStrictlyOrdered(self, workload):
        isStrictlyOrdered = True

        for i in range(len(self.cores)):
            meanTimes = []

            for j in range(len(self.frequencies[i])):
                anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

                meanTimes.append(int(statistics.mean(workload["time"][anchor:anchor + len(self.pmus)])))

            isStrictlyOrdered &= len(meanTimes) == len(set(meanTimes))

        return isStrictlyOrdered

    def _isTimeLarge(self, workload):
        isSmall = False

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                if (j <= 1):
                    anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)

                    isSmall |= statistics.mean(workload["time"][anchor:anchor + len(self.pmus)]) < 1.0

        return not isSmall

    def _classify(self):
        cpuBounds = []
        memBounds = []
        ioBounds = []
        others = []

        for workload in self.workloads:
            if ():
                cpuBounds.append(workload)
            elif ():
                memBounds.append(workload)
            elif ():
                ioBounds.append(workload)
            else:
                others.append(workload)

        return self.workloads or cpuBounds or memBounds or ioBounds or others


if __name__ == "__main__":

    main()
