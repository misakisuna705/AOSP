# !/usr/bin/env python3

import subprocess


class Profiler(object):

    def __init__(self) -> None:
        pass

    def profile(self):

        # get all types of raw pmus
        raws = subprocess.run(
            ["adb", "shell", "simpleperf", "list", "raw", "|", "grep", "raw-", "|", "awk", "'{print $1}'"],
            stdout=subprocess.PIPE,
        ).stdout.decode('utf-8').splitlines()

        # parameter
        simpleperf = "simpleperf stat --use-devfreq-counters --per-core"
        benchmark = {"MiBench": "/data/local/tmp/Mibench/bitcnts 102400000"}

        j = 0

        # get all counters of raw pmus
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
