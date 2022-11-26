#! /usr/bin/env python3

import csv
import logging
import statistics

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s line:%(lineno)-3d %(levelname)-8s ] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)


def main():
    # selector = PerFreqSelector()
    selector = PerCoreSelector()

    selector.select(6)


class _Selector(object):

    def __init__(self) -> None:
        self.sheets = [
            "bin/Dhrystone/dry.csv", "bin/LMbench/bw_mem/512m/bcopy.csv", "bin/LMbench/bw_mem/512m/bzero.csv", "bin/LMbench/bw_mem/512m/cp.csv",
            "bin/LMbench/bw_mem/512m/fcp.csv", "bin/LMbench/bw_mem/512m/frd.csv", "bin/LMbench/bw_mem/512m/rd.csv", "bin/Mibench/bitcnts/84600000.csv",
            "bin/SpecCpu2006/400.perlbench.csv", "bin/SpecCpu2006/401.bzip2.csv", "bin/SpecCpu2006/403.gcc.csv", "bin/SpecCpu2006/429.mcf.csv",
            "bin/SpecCpu2006/433.milc.csv", "bin/SpecCpu2006/444.namd.csv", "bin/SpecCpu2006/445.gobmk.csv", "bin/SpecCpu2006/447.dealII.csv",
            "bin/SpecCpu2006/450.soplex.csv", "bin/SpecCpu2006/453.povray.csv", "bin/SpecCpu2006/456.hmmer.csv", "bin/SpecCpu2006/458.sjeng.csv",
            "bin/SpecCpu2006/462.libquantum.csv", "bin/SpecCpu2006/464.h264ref.csv", "bin/SpecCpu2006/470.lbm.csv", "bin/SpecCpu2006/471.omnetpp.csv",
            "bin/SpecCpu2006/473.astar.csv", "bin/SpecCpu2006/482.sphinx3.csv", "bin/SpecCpu2006/483.xalancbmk.csv", "bin/SpecCpu2017/600.perlbench_s.csv",
            "bin/SpecCpu2017/602.gcc_s.csv", "bin/SpecCpu2017/605.mcf_s.csv", "bin/SpecCpu2017/619.lbm_s.csv", "bin/SpecCpu2017/620.omnetpp_s.csv",
            "bin/SpecCpu2017/623.xalancbmk_s.csv", "bin/SpecCpu2017/625.x264_s.csv", "bin/SpecCpu2017/638.imagick_s.csv", "bin/SpecCpu2017/641.leela_s.csv",
            "bin/SpecCpu2017/644.nab_s.csv", "bin/SpecCpu2017/657.xz_s.csv"
        ]

        # print(len(self.sheets))

        self.workloads = []

        for sheet in self.sheets:
            with open(sheet, newline="") as f:
                rows = csv.DictReader(f)

                self.workloads.append([row for row in rows])

        # print(self.workloads[0])

        self.cores = sorted(set([row["setup core"] for row in self.workloads[0]]))

        # print(self.cores)

        self.frequencies = []

        # print(self.frequencies)

        for core in self.cores:
            self.frequencies.append(sorted(set([int(row["frequency"]) for row in self.workloads[0] if row["setup core"] == core])))

        self.pmus = sorted(set([row["event"] for row in self.workloads[0]]))

        # print(self.pmus)

        for workload in self.workloads:
            for i in range(len(self.cores)):
                for j in range(len(self.frequencies[i])):
                    for k in range(len(self.pmus)):
                        row = workload[i * len(workload) // len(self.cores) + j * len(self.pmus) + k]

                        row["count"] = int(row["count"].replace(',', ''))
                        row["time"] = float(row["time"].replace(',', ''))

        # print(self.workloads[0])

    def rSquare(self, listA, listB):
        cov = statistics.covariance(listA, listB)
        stDevProduct = statistics.stdev(listA) * statistics.stdev(listB)

        return pow(cov / stDevProduct, 2) if stDevProduct else False


class PerFreqSelector(_Selector):

    def __init__(self) -> None:
        super().__init__()

    def select(self, num):
        ranks = self._rank()
        dataset = self._format(ranks, num)

        return dataset

    def _rank(self):
        ranks = [[[{"pmu": (), "samples": [], "correlation": 0.0} for k in range(len(self.pmus))] for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for workload in self.workloads:
            for i in range(len(self.cores)):
                for j in range(len(self.frequencies[i])):
                    for k in range(len(self.pmus)):
                        row = workload[i * len(workload) // len(self.cores) + j * len(self.pmus) + k]

                        ranks[i][j][k]["pmu"] = (k, self.pmus[k])
                        ranks[i][j][k]["samples"].append((row["count"], row["time"]))

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                for k in range(len(self.pmus)):
                    count = [sample[0] for sample in ranks[i][j][k]["samples"]]
                    time = [sample[1] for sample in ranks[i][j][k]["samples"]]

                    ranks[i][j][k]["correlation"] = self.rSquare(count, time)

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                ranks[i][j] = sorted(ranks[i][j], key=lambda dict: dict["correlation"], reverse=True)

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                for k in range(len(self.pmus)):
                    print(self.cores[i], self.frequencies[i][j], ranks[i][j][k]["pmu"], ranks[i][j][k]["correlation"])
                print("")

        return ranks

    def _format(self, ranks, num):
        dataset = [[[] for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                qualifiers = []
                meanTimes = []

                for k in range(num):
                    counts = []

                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + j * len(self.pmus)
                        row = workload[anchor + ranks[i][j][k]["pmu"][0]]

                        meanTime = statistics.mean([row["time"] for row in workload[anchor:anchor + len(self.pmus)]])

                        qualifiers.append(row["event"]) if (row["event"] not in qualifiers) else None
                        counts.append(row["count"])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                    dataset[i][j].append({qualifiers[k]: counts})

                dataset[i][j].append({"times": meanTimes})

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                print("cores: ", self.cores[i], "frequencies: ", self.frequencies[i][j])
                print("")

                for item in dataset[i][j]:
                    print(item)
                    print("")
                print("")
            print("")

        return dataset


class PerCoreSelector(_Selector):

    def __init__(self) -> None:
        super().__init__()

    def select(self, num):
        perCoreRanks = [[{"pmu": (), "samples": [], "correlation": 0.0} for j in range(len(self.pmus))] for i in range(len(self.cores))]

        for workload in self.workloads:
            for i in range(len(self.cores)):
                for j in range(len(self.pmus)):
                    perCoreRanks[i][j]["pmu"] = (j, self.pmus[j])

                    for k in range(len(self.frequencies[i])):
                        row = workload[i * len(workload) // len(self.cores) + k * len(self.pmus) + j]

                        perCoreRanks[i][j]["samples"].append((row["count"], row["time"]))

        for i in range(len(self.cores)):
            for j in range(len(self.pmus)):
                count = [sample[0] for sample in perCoreRanks[i][j]["samples"]]
                time = [sample[1] for sample in perCoreRanks[i][j]["samples"]]

                perCoreRanks[i][j]["correlation"] = self.rSquare(count, time)

        for i in range(len(self.cores)):
            perCoreRanks[i] = sorted(perCoreRanks[i], key=lambda dict: dict["correlation"], reverse=True)

        for i in range(len(self.cores)):
            for j in range(len(self.pmus)):
                print(self.cores[i], perCoreRanks[i][j]["pmu"], perCoreRanks[i][j]["correlation"])
            print("")

        perCoreDataset = [[] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            qualifiers = []
            meanTimes = []

            for j in range(num):
                counts = []

                for k in range(len(self.frequencies[i])):
                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + k * len(self.pmus)
                        row = workload[anchor + perCoreRanks[i][j]["pmu"][0]]

                        meanTime = statistics.mean([row["time"] for row in workload[anchor:anchor + len(self.pmus)]])

                        qualifiers.append(row["event"]) if (row["event"] not in qualifiers) else None
                        counts.append(row["count"])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                perCoreDataset[i].append({qualifiers[j]: counts})

            perCoreDataset[i].append({"times": meanTimes})

        for i in range(len(self.cores)):
            print("cores: ", self.cores[i])
            print("")

            for item in perCoreDataset[i]:
                print(item)
                print("")
            print("")

        return perCoreDataset


if __name__ == "__main__":

    main()
