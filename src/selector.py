#! /usr/bin/env python3

import csv
import logging
from statistics import mean

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s line:%(lineno)-3d %(levelname)-8s ] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)


class Selector(object):

    def __init__(self) -> None:
        pass

    def select(self, num):
        sheets = [
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

        # print(len(sheets))

        workloads = []

        for sheet in sheets:
            with open(sheet, newline="") as f:
                rows = csv.DictReader(f)

                workloads.append([row for row in rows])

        # print(workloads[0])

        cores = sorted(set([row["setup core"] for row in workloads[0]]))

        # print(cores)

        frequencies = []

        # print(frequencies)

        for core in cores:
            frequencies.append(sorted(set([int(row["frequency"]) for row in workloads[0] if row["setup core"] == core])))

        pmus = sorted(set([row["event"] for row in workloads[0]]))

        # print(pmus)

        for workload in workloads:
            for i in range(len(cores)):
                for j in range(len(frequencies[i])):
                    for k in range(len(pmus)):
                        row = workload[i * len(workload) // len(cores) + j * len(pmus) + k]

                        row["count"] = int(row["count"].replace(',', ''))
                        row["time"] = float(row["time"].replace(',', ''))

        # print(workloads[0])

        datalist = [[[{"pmu": (), "samples": [], "correlation": 0.0} for k in range(len(pmus))] for j in range(len(frequencies[i]))] for i in range(len(cores))]

        for workload in workloads:
            for i in range(len(cores)):
                for j in range(len(frequencies[i])):
                    for k in range(len(pmus)):
                        row = workload[i * len(workload) // len(cores) + j * len(pmus) + k]

                        datalist[i][j][k]["pmu"] = (k, pmus[k])
                        datalist[i][j][k]["samples"].append((row["count"], row["time"]))

        def rSquare(listA, listB):
            covariance = sum([(x - mean(listA)) * (y - mean(listB)) for x, y in zip(listA, listB)])
            stdDeviationProduct = (sum([(x - mean(listA))**2 for x in listA]) * sum([(y - mean(listB))**2 for y in listB]))**0.5

            return (covariance / stdDeviationProduct)**2 if stdDeviationProduct else 0

        for i in range(len(cores)):
            for j in range(len(frequencies[i])):
                for k in range(len(pmus)):
                    count = [sample[0] for sample in datalist[i][j][k]["samples"]]
                    time = [sample[1] for sample in datalist[i][j][k]["samples"]]

                    datalist[i][j][k]["correlation"] = rSquare(count, time)

        for i in range(len(cores)):
            for j in range(len(frequencies[i])):
                datalist[i][j] = sorted(datalist[i][j], key=lambda dict: dict["correlation"], reverse=True)

        # for i in range(len(cores)):
        # for j in range(len(frequencies[i])):
        # for k in range(len(pmus)):
        # print(cores[i], frequencies[i][j], datalist[i][j][k]["pmu"], datalist[i][j][k]["correlation"])
        # print("")

        rankset = [[[] for j in range(len(frequencies[i]))] for i in range(len(cores))]

        for i in range(len(cores)):
            for j in range(len(frequencies[i])):
                counts = []
                meanTimes = []
                qualifiers = []

                for workload in workloads:
                    anchor = i * len(workload) // len(cores) + j * len(pmus)

                    meanTimes.append(mean([row["time"] for row in workload[anchor:anchor + len(pmus)]]))

                    for k in range(num):
                        row = workload[anchor + datalist[i][j][k]["pmu"][0]]

                        counts.append(row["count"])

                        if (row["event"] not in qualifiers): 
                            qualifiers.append(row["event"])

                rankset[i][j].append((counts, meanTimes, qualifiers))

        for i in range(len(cores)):
            for j in range(len(frequencies[i])):
                print("cores: ", cores[i], "frequencies: ", frequencies[i][j])
                print("")

                for thing in rankset[i][j]:
                    print("counts: ", thing[0])
                    print("")
                    print("times: ", thing[1])
                    print("")
                    print("qualifiers: ", thing[2])
                    print("")
                print("")

        return rankset


def main():
    selector = Selector()

    selector.select(6)


if __name__ == "__main__":
    main()
