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
    perFreqSelector = PerFreqSelector()
    perCoreSelector = PerCoreSelector()

    perFreqSelector.select(6)
    perCoreSelector.select(6)


class _Selector(object):

    def __init__(self) -> None:
        self.sheets = [
            "dat/Dhrystone/dry.csv",
            \
            "dat/LMbench/bw_mem/512m/bcopy.csv", "dat/LMbench/bw_mem/512m/bzero.csv", "dat/LMbench/bw_mem/512m/cp.csv",
            "dat/LMbench/bw_mem/512m/fcp.csv", "dat/LMbench/bw_mem/512m/frd.csv", "dat/LMbench/bw_mem/512m/rd.csv", "dat/Mibench/bitcnts/84600000.csv",
            \
            "dat/SpecCpu2006/400.perlbench.csv", "dat/SpecCpu2006/401.bzip2.csv", "dat/SpecCpu2006/403.gcc.csv", "dat/SpecCpu2006/429.mcf.csv",
            "dat/SpecCpu2006/433.milc.csv", "dat/SpecCpu2006/444.namd.csv", "dat/SpecCpu2006/445.gobmk.csv", "dat/SpecCpu2006/447.dealII.csv",
            "dat/SpecCpu2006/450.soplex.csv", "dat/SpecCpu2006/453.povray.csv", "dat/SpecCpu2006/456.hmmer.csv", "dat/SpecCpu2006/458.sjeng.csv",
            "dat/SpecCpu2006/462.libquantum.csv", "dat/SpecCpu2006/464.h264ref.csv", "dat/SpecCpu2006/470.lbm.csv", "dat/SpecCpu2006/471.omnetpp.csv",
            "dat/SpecCpu2006/473.astar.csv", "dat/SpecCpu2006/482.sphinx3.csv", "dat/SpecCpu2006/483.xalancbmk.csv",
            \
            "dat/SpecCpu2017/600.perlbench_s.csv", "dat/SpecCpu2017/602.gcc_s.csv", "dat/SpecCpu2017/605.mcf_s.csv", "dat/SpecCpu2017/619.lbm_s.csv",
            "dat/SpecCpu2017/620.omnetpp_s.csv", "dat/SpecCpu2017/623.xalancbmk_s.csv", "dat/SpecCpu2017/625.x264_s.csv", "dat/SpecCpu2017/638.imagick_s.csv",
            "dat/SpecCpu2017/641.leela_s.csv", "dat/SpecCpu2017/644.nab_s.csv", "dat/SpecCpu2017/657.xz_s.csv"
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

    def select(self, num):
        ranks = self._rank()
        dataset = self._format(ranks, num)

        return dataset


class PerFreqSelector(_Selector):

    def __init__(self) -> None:
        super().__init__()

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

        # for i in range(len(self.cores)):
        # for j in range(len(self.frequencies[i])):
        # print("cores: ", self.cores[i], "frequencies: ", self.frequencies[i][j])
        # print("")

        # for item in dataset[i][j]:
        # print(item)
        # print("")
        # print("")
        # print("")

        data = [[{} for j in range(len(self.frequencies[i]))] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            for j in range(len(self.frequencies[i])):
                for item in dataset[i][j]:
                    data[i][j] |= item

        # for i in range(len(self.cores)):
        # for j in range(len(self.frequencies[i])):
        # print("cores: ", self.cores[i], "frequencies: ", self.frequencies[i][j])
        # print("")

        # print(data[i][j])
        # print("")
        # print("")

        return data


class PerCoreSelector(_Selector):

    def __init__(self) -> None:
        super().__init__()

    def _rank(self):
        ranks = [[{"pmu": (), "samples": [], "correlation": 0.0} for j in range(len(self.pmus))] for i in range(len(self.cores))]

        for workload in self.workloads:
            for i in range(len(self.cores)):
                for j in range(len(self.pmus)):
                    ranks[i][j]["pmu"] = (j, self.pmus[j])

                    for k in range(len(self.frequencies[i])):
                        row = workload[i * len(workload) // len(self.cores) + k * len(self.pmus) + j]

                        ranks[i][j]["samples"].append((row["count"], row["time"]))

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
        dataset = [[] for i in range(len(self.cores))]

        for i in range(len(self.cores)):
            qualifiers = []
            meanTimes = []

            for j in range(num):
                counts = []

                for k in range(len(self.frequencies[i])):
                    for workload in self.workloads:
                        anchor = i * len(workload) // len(self.cores) + k * len(self.pmus)
                        row = workload[anchor + ranks[i][j]["pmu"][0]]

                        meanTime = statistics.mean([row["time"] for row in workload[anchor:anchor + len(self.pmus)]])

                        qualifiers.append(row["event"]) if (row["event"] not in qualifiers) else None
                        counts.append(row["count"])
                        meanTimes.append(meanTime) if (meanTime not in meanTimes) else None

                dataset[i].append({qualifiers[j]: counts})

            dataset[i].append({"times": meanTimes})

        # for i in range(len(self.cores)):
        # print("cores: ", self.cores[i])
        # print("")

        # for item in dataset[i]:
        # print(item)
        # print("")
        # print("")

        return dataset


if __name__ == "__main__":

    main()
