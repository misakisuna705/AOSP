#! /usr/bin/env python3

import argparse
import csv
import re
import subprocess


class Profiler(object):

    def __init__(self) -> None:
        pass

    def profile(self, benchmark, outputfile):
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

        # set simpleperf parameters
        simpleperf = "simpleperf stat --use-devfreq-counters --per-core"

        # log
        print("\n set simpleperf: ")
        print(simpleperf)
        print("\nset benchmark: ")
        print(benchmark)
        print("\nset outputfile: ")
        print(outputfile)
        print("\n")

        sheet = [["setup core", "runtime core", "frequency", "coverage", "event", "count", "time"]]

        for idx, policy in enumerate(policies):
            core = re.findall(r'\d+', policy)[0]
            mask = format(1 << int(core), "02x")

            # log
            print("\nset cluster")
            print(idx)
            print("\nset core: ")
            print(core)
            print("\nset mask: ")
            print(mask)
            print("\n")

            for frequency in [frequencies[idx][0], frequencies[idx][int((len(frequencies[idx]) - 1) / 2)], frequencies[idx][-1]]:
                # log
                print("\nprepared frequency: ")
                print(frequency)
                print("\n")

                # set policy parameters
                subprocess.run(["adb", "shell", "echo 0 > /sys/devices/system/cpu/cpufreq/" + policy + "/scaling_min_freq"])
                subprocess.run(["adb", "shell", "echo 99999999 > /sys/devices/system/cpu/cpufreq/" + policy + "/scaling_max_freq"])
                subprocess.run(["adb", "shell", "echo " + governor + " > /sys/devices/system/cpu/cpufreq/" + policy + "/scaling_governor"])

                # log
                print("\nset governor: ")
                subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpufreq/policy*/scaling_governor"])
                print("\n")

                # set frequency parameters
                subprocess.run(["adb", "shell", "echo " + frequency + " > /sys/devices/system/cpu/cpufreq/" + policy + "/scaling_min_freq"])
                subprocess.run(["adb", "shell", "echo " + frequency + " > /sys/devices/system/cpu/cpufreq/" + policy + "/scaling_max_freq"])

                # log
                print("\nset min frequency: ")
                subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_min_freq"])
                print("\nset max frequency: ")
                subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq"])
                print("\nset cur frequency: ")
                subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq"])
                print("\n")

                # set taskset
                taskset = "taskset " + mask

                # output all counters of raw pmus
                for i in range(0, len(raws), 6):
                    pmus = ",".join(raws[i:i + 6])

                    datas = [
                        j for j in [
                            k.split() for k in filter(
                                None,
                                subprocess.run(["adb", "shell", taskset, simpleperf, "-e", pmus, benchmark], stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines())
                        ] if (j[0] == core or j[0] == 'Total')
                    ]

                    # log
                    print("\ncommand: ")
                    print("adb", "shell", taskset, simpleperf, "-e", pmus, benchmark)
                    print("\n")

                    # out sheet of all counters
                    for j in range(0, len(datas)):
                        if datas[j][0] == core:
                            sheet.append([core, datas[j][0], frequency, datas[j][-1].replace("(", "").replace(")", ""), datas[j][2], datas[j][1], datas[-1][3]])

                    # log
                    for j in range(len(sheet)):
                        print('\t'.join(sheet[j]))
                    print("\n")

        # output csv of sheet
        with open(outputfile, "w") as f:
            w = csv.writer(f, dialect='excel')

            w.writerows(sheet)


def main(argv):
    profiler = Profiler()

    # set benchmark parameters
    # set outputfile parameters
    profiler.profile(argv.benchmark[0], argv.outputfile[0])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    group = parser.add_argument_group()

    group.add_argument("-b", "--benchmark", nargs=1, type=str, help="string of benchmark command")
    group.add_argument("-o", "--outputfile", nargs=1, type=str, help="string of path to csv file")

    argv = parser.parse_args()

    if not argv.benchmark or not argv.outputfile:
        parser.error("Should have both benchmark and outputfile")

    main(argv)
