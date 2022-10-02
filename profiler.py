# !/usr/bin/env python3

import subprocess


class Profiler(object):

    def __init__(self) -> None:
        pass

    def profile(self):

        raws = subprocess.run(
            ["adb", "shell", "simpleperf", "list", "raw", "|", "grep", "raw-", "|", "awk", "'{print $1}'"],
            stdout=subprocess.PIPE,
        ).stdout.decode('utf-8').splitlines()

        print(raws)

        print("")

        simpleperf = "simpleperf stat --use-devfreq-counters --per-core"
        benchmark = {"MiBench": "/data/local/tmp/Mibench/bitcnts 102400000"}

        j = 0

        for i in range(0, len(raws), 6):
            pmus = raws[i] + "," + raws[i + 1] + "," + raws[i + 2] + "," + raws[i + 3] + "," + raws[i + 4] + "," + raws[i + 5]

            count = subprocess.run(["adb", "shell", simpleperf, "--group", pmus, benchmark["MiBench"]],
                                   stdout=subprocess.PIPE).stdout.decode('utf-8')

            print(count)

            j += 1

            print("")

            print(j)

            print("")


def main():
    profiler = Profiler()
    profiler.profile()


if __name__ == "__main__":
    main()
