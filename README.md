# Android Open Source Project

<!-- vim-markdown-toc GFM -->

* [QuickStart](#quickstart)
    - [環境](#環境)
    - [執行](#執行)
* [Reference](#reference)
    - [AOSP](#aosp)
    - [Benchmark](#benchmark)
    - [Profiler](#profiler)
* [Deprecated](#deprecated)
    - [MediaBench](#mediabench)
        + [H.264](#h264)
        + [JPEG-2000](#jpeg-2000)
    - [Geekbench](#geekbench)
        + [binary](#binary)
            * [刷入](#刷入)
            * [執行](#執行-1)
        + [apk](#apk)
            * [刷入](#刷入-1)
            * [執行](#執行-2)

<!-- vim-markdown-toc -->

---

## QuickStart

### 環境

-   python 3.10.8
-   pipenv
    -   pandas
    -   sklearn

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
pipenv run python3 main.py
```

---

## Reference

### AOSP

-   [Pixel 4a](doc/aosp.md)

### Benchmark

-   [Dhrystone](https://github.com/misakisuna705/Dhrystone)
-   [LMbench](https://github.com/misakisuna705/LMbench)
-   [MiBench](https://github.com/misakisuna705/MiBench)
-   [SPEC CPU® 2006](https://github.com/misakisuna705/SPEC-CPU-2006)
-   [SPEC CPU® 2017](https://github.com/misakisuna705/SPEC-CPU-2017)

### Profiler

-   [CpuFreq](doc/cpufreq.md)
-   [Simpleperf](https://github.com/misakisuna705/Simpleperf)

```zsh
python3 profiler.py [-h] [-b BENCHMARK] [-o OUTPUTFILE]
```

---

## Deprecated

### [MediaBench](https://github.com/misakisuna705/MediaBench)

#### H.264

```zsh
adb push mediaBench/mb2_vid_h264 /data/local/tmp/MediaBench/mb2_vid_h264
```

#### JPEG-2000

```zsh
adb push mediaBench/mb2_vid_jpg2000 /data/local/tmp/MediaBench/mb2_vid_jpg2000
```

### [Geekbench](https://github.com/misakisuna705/Geekbench)

#### binary

##### 刷入

```zsh
adb push aarch64-linux-gnu /data/local/tmp/Geekbench

adb push geekbench/Geekbench-5.4.0-LinuxARMPreview/geekbench_aarch64 /data/local/tmp/Geekbench
adb push geekbench/Geekbench-5.4.0-LinuxARMPreview/geekbench5 /data/local/tmp/Geekbench
adb push geekbench/Geekbench-5.4.0-LinuxARMPreview/geekbench_armv7 /data/local/tmp/Geekbench
adb push geekbench/Geekbench-5.4.0-LinuxARMPreview/geekbench.plar /data/local/tmp/Geekbench

adb push geekbench/Geekbench-5.4.0-LinuxARMPreview /data/local/tmp/Geekbench
```

##### 執行

```zsh
adb shell LD_LIBRARY_PATH=/data/local/tmp/Geekbench/aarch64-linux-gnu /data/local/tmp/Geekbench/aarch64-linux-gnu/ld-linux-aarch64.so.1 /data/local/tmp/Geekbench/Geekbench-5.4.0-LinuxARMPreview/geekbench_aarch64
```

#### apk

-   安裝 Java 並在 shell profile 配置 openjdk 路徑
-   安裝 Android Studio 並在 shell profile 配置 Android sdk 的 build-tools 路徑

```zsh
pip install wlauto # 安裝[workload-automation](https://github.com/ARM-software/workload-automation)
```

##### 刷入

```zsh
adb install-multiple geekbench/Geekbench\ 4_4.4.2_Apkpure/*.apk
```

##### 執行

```zsh
wa run -f -c geekbench/Geekbench\ 4_4.4.2_Apkpure/geekbench.yaml geekbench
```
