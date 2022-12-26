# Android Open Source Project

<!-- vim-markdown-toc GFM -->

* [QuickStart](#quickstart)
    - [參數](#參數)
        + [系統](#系統)
        + [目標](#目標)
    - [環境](#環境)
    - [執行](#執行)
    - [架構](#架構)
* [Reference](#reference)
    - [AOSP](#aosp)
    - [Benchmark](#benchmark)
    - [Profiling Tool](#profiling-tool)

<!-- vim-markdown-toc -->

---

## QuickStart

### 參數

#### 系統

-   Ubuntu 18.04

#### 目標

-   arm64

### 環境

-   adb
-   python 3.10.8
    -   pipenv # pipenv graph
        -   matplotlib
        -   scikit-learn
        -   statsmodels

### 執行

```zsh
# setup
adb push res/Dhrystone/v2.2/dry /data/local/tmp/Dhrystone/dry
adb push res/LMbench/bin/aarch64 /data/local/tmp/LMbench
adb push res/Mibench /data/local/tmp
adb push res/SpecCpu2006 /data/local/tmp
adb push res/SpecCpu2017 /data/local/tmp

# profile
./test.sh

# run
pipenv run python3 main.py -d "dat/26/Pixel4a/Doshin"
```

### 架構

```zsh
.
├── main.py             # pipenv run python3 main.py [-h] [-d DIRECTORY]
├── src
│   ├── profiler.py     # pipenv run python3 src/profiler.py [-h] [-b BENCHMARK] [-o OUTPUTFILE]
│   ├── preprocessor.py
│   ├── formatter.py
│   └── estimator.py
├── res
│   ├── Dhrystone
│   ├── LMbench
│   ├── Mibench
│   ├── SpecCpu2006
│   └── SpecCpu2017
├── dat
│   ├── Doshin
│   ├── Essen
│   ├── Peihsuan
│   └── Weichun
└── bin
    └── (None)
```

## Reference

### AOSP

-   [Pixel 4a](doc/aosp.md)

### Benchmark

-   [Dhrystone](https://github.com/misakisuna705/Dhrystone)
-   [LMbench](https://github.com/misakisuna705/LMbench)
-   [MiBench](https://github.com/misakisuna705/MiBench)
-   [SPEC CPU® 2006](https://github.com/misakisuna705/SPEC-CPU-2006)
-   [SPEC CPU® 2017](https://github.com/misakisuna705/SPEC-CPU-2017)

### Profiling Tool

-   [CpuFreq](doc/cpufreq.md)
-   [Simpleperf](https://github.com/misakisuna705/Simpleperf)
