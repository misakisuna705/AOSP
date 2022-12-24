#! /usr/bin/env python3


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
        for workload in self.workloads:
            if ():
                self.workloads.remove(workload)

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
