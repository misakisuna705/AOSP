# !/usr/bin/env python3

import subprocess


class Profiler(object):

    def __init__(self) -> None:
        pass

    def profile(self):
        # get all types of scaling governor
        governors = (subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors"],
                                    stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines())[0].split()

        print("\n", governors, "\n")

        # get all types of policies corresponding to their cluster
        policies = subprocess.run(["adb", "shell", "ls /sys/devices/system/cpu/cpufreq"], stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()

        print("\n", policies, "\n")

        # get the set of frequncies corresponding to their cluster
        frequencies = [
            element.split() for element in list(
                set([
                    i for i in subprocess.run(["adb", "shell", "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_frequencies"],
                                              stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()
                ]))
        ]

        # frequencies = [element.split() for element in frequencies]

        print("\n", frequencies, "\n")

        # get all types of raw pmus
        raws = subprocess.run(["adb", "shell", "simpleperf", "list", "raw", "|", "grep", "raw-", "|", "awk", "'{print $1}'"],
                              stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()

        j = 0

        print("\n", raws, "\n")

        # set policy parameters

        # adb shell "echo 0 > /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"
        # adb shell "echo 99999999 > /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"
        # adb shell "echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"

        # set policy parameters

        # adb shell "echo 1804800 > /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"
        # adb shell "echo 1804800 > /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"

        # subprocess.run([
        # "adb",
        # "shell",
        # "echo",
        # frequency,
        # ])

        # set benchmark parameters
        benchmark = {"MiBench": "/data/local/tmp/Mibench/bitcnts 102400000"}

        # set simpleperf parameters
        simpleperf = "simpleperf stat --use-devfreq-counters --per-core"

        # ouput all counters of raw pmus
        for i in range(0, len(raws), 6):
            pmus = ",".join(raws[i:i + 6])

            info = subprocess.run(["adb", "shell", simpleperf, "--group", pmus, benchmark["MiBench"]], stdout=subprocess.PIPE).stdout.decode('utf-8')

            print(info)

            j += 1

            print("")
            print(j)
            print("")


def main():
    profiler = Profiler()
    profiler.profile()


if __name__ == "__main__":
    main()
