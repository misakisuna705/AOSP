#! /usr/bin/env python3


def main(argv):
    pass


class _Preprocessor(object):

    def __init__(self, workloads) -> None:

        self.workloads = workloads

        # print(self.workloads[0])

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
        # print(self.workloads)
        # print(self.cores)
        # print(self.frequencies)
        # print(self.pmus)

        return self.workloads


if __name__ == "__main__":

    main()
