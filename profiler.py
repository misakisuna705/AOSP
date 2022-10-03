# !/usr/bin/env python3

import subprocess
import csv


class Profiler(object):

    def __init__(self) -> None:
        pass

    def profile(self):
        # get all types of scaling governor
        governors = (subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors"],
                                    stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines())[0].split()

        # log
        print("\n", governors, "\n")

        # get all types of policies corresponding to their cluster
        policies = subprocess.run(["adb", "shell", "ls /sys/devices/system/cpu/cpufreq"], stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()

        # log
        print("\n", policies, "\n")

        # get the set of frequncies corresponding to their cluster
        frequencies = [
            i.split() for i in list(
                sorted(
                    set([
                        j for j in subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_frequencies"],
                                                  stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()
                    ])))
        ]

        # log
        print("\n", frequencies, "\n")

        # get all types of raw pmus
        raws = subprocess.run(["adb", "shell", "simpleperf", "list", "raw", "|", "grep", "raw-", "|", "awk", "'{print $1}'"],
                              stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()

        # log
        print("\n", raws, "\n")

        # self-defined parameters
        governor = governors[2]
        policy = policies[0]
        frequency = frequencies[0][9]
        core = '01'

        # set policy parameters
        subprocess.run(["adb", "shell", "echo 0 > /sys/devices/system/cpu/cpufreq/" + policy + "/scaling_min_freq"])
        subprocess.run(["adb", "shell", "echo 99999999 > /sys/devices/system/cpu/cpufreq/" + policy + "/scaling_max_freq"])
        subprocess.run(["adb", "shell", "echo " + governor + " > /sys/devices/system/cpu/cpufreq/" + policy + "/scaling_governor"])

        # log
        print("\n")
        subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpufreq/policy*/scaling_governor"])
        print("\n")

        # set frequency parameters
        subprocess.run(["adb", "shell", "echo " + frequency + " > /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"])
        subprocess.run(["adb", "shell", "echo " + frequency + " > /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"])

        # log
        print("\n")
        subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_min_freq"])
        print("\n")
        subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq"])
        print("\n")
        subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq"])
        print("\n")
        print(core)
        print("\n")

        # set benchmark parameters
        benchmark = {"MiBench": "/data/local/tmp/Mibench/bitcnts 102400000"}

        # set simpleperf parameters
        simpleperf = "simpleperf stat --use-devfreq-counters --per-core"

        # ouput all counters of raw pmus
        zzz = 0

        sheet = [["core", "coverage", "event", "count", "time"]]

        for i in range(0, len(raws), 6):
            pmus = ",".join(raws[i:i + 6])

            datas = [
                j for j in [
                    k.split() for k in filter(
                        None,
                        subprocess.run(["adb", "shell", "taskset " +
                                        core, simpleperf, "-e", pmus, benchmark["MiBench"]], stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines())
                ] if (j[0] == "0" or j[0] == 'Total')
            ]

            for j in range(0, len(datas)):
                if datas[j][0] == "0":
                    sheet.append([datas[j][0], datas[j][-1].replace("(", "").replace(")", ""), datas[j][2], datas[j][1], datas[-1][3]])

            for j in range(len(sheet)):
                print('\t'.join(sheet[j]))

            print("")
            print(len(sheet) - 1)
            print("")
            zzz += 1
            print(zzz)
            print("")

        # ouput csv of all counters
        with open("infos.csv", "w") as f:
            w = csv.writer(f, dialect='excel')

            w.writerows(sheet)


def main():
    profiler = Profiler()
    profiler.profile()


if __name__ == "__main__":
    main()
