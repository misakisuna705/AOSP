# Android Open Source Project

<!-- vim-markdown-toc GFM -->

* [參數](#參數)
    - [系統](#系統)
    - [目標](#目標)
        + [Pixel](#pixel)
            * [Pixel 3 / Pixel 3XL](#pixel-3--pixel-3xl)
            * [Pixel 4 / Pixel 4XL](#pixel-4--pixel-4xl)
            * [Pixel 4a](#pixel-4a)
        + [Android 12](#android-12)
* [環境](#環境)
    - [git](#git)
    - [repo](#repo)
    - [python3](#python3)
    - [others](#others)
* [AOSP](#aosp)
    - [代碼同步](#代碼同步)
    - [驅動導入](#驅動導入)
        + [Google](#google)
        + [Qualcomm](#qualcomm)
    - [專案構建](#專案構建)
    - [映像刷機（Android Debug Bridge）](#映像刷機android-debug-bridge)
        + [安裝](#安裝)
        + [刷入](#刷入)
        + [提權](#提權)
* [Benchmark](#benchmark)
    - [LMbench](#lmbench)
        + [刷入](#刷入-1)
    - [MiBench](#mibench)
        + [刷入](#刷入-2)
    - [Dhrystone](#dhrystone)
        + [刷入](#刷入-3)
    - [MediaBench（Deprecated）](#mediabenchdeprecated)
        + [H.264](#h264)
            * [刷入](#刷入-4)
            * [執行](#執行)
        + [JPEG-2000](#jpeg-2000)
            * [刷入](#刷入-5)
            * [執行](#執行-1)
    - [Geekbench（Deprecated）](#geekbenchdeprecated)
        + [binary](#binary)
            * [刷入](#刷入-6)
            * [執行](#執行-2)
        + [apk](#apk)
            * [刷入](#刷入-7)
            * [執行](#執行-3)
    - [SPEC CPU® 2017](#spec-cpu-2017)
        + [刷入](#刷入-8)
    - [SPEC CPU® 2006](#spec-cpu-2006)
        + [刷入](#刷入-9)
* [Profiler](#profiler)
    - [執行](#執行-4)
* [info](#info)
    - [paper](#paper)
    - [doc](#doc)
    - [stackoverflow](#stackoverflow)

<!-- vim-markdown-toc -->

---

## 參數

### 系統

-   Ubuntu 18.04（WSL）

### 目標

#### [Pixel](https://zh.wikipedia.org/zh-tw/Google_Pixel)

##### Pixel 3 / Pixel 3XL

| CPU                       |                         | GPU        |
| ------------------------- | ----------------------- | ---------- |
| Qualcomm® Snapdragon™ 845 |                         | Adreno 630 |
| LITTLE cluster            | big cluster             |            |
| 4x Kryo 385 Silver 1.8GHz | 4x Kryo 385 Gold 2.8GHz |            |
| Cortex-A55                | Cortex-A75              |            |
| 6 PMU counters            | 6 PMU counters          |            |

##### Pixel 4 / Pixel 4XL

| CPU                       |                          |                           | GPU        |
| ------------------------- | ------------------------ | ------------------------- | ---------- |
| Qualcomm® Snapdragon™ 855 |                          |                           | Adreno 640 |
| LITTLE cluster            | big cluster              | Prime cluster             |            |
| 4x Kryo 485 Silver 1.8GHz | 3x Kryo 485 Gold 2.42GHz | 1x Kryo 485 Prime 2.84GHz |            |
| Cortex-A55                | Cortex-A76               | Cortex-A76                |            |
| 6 PMU counters            | 6 PMU counters           | 6 PMU counters            |            |

##### Pixel 4a

-   CPU

| CPU                        |                        | GPU        |
| -------------------------- | ---------------------- | ---------- |
| Qualcomm® Snapdragon™ 730G |                        | Adreno 618 |
| LITTLE cluster             | big cluster            |            |
| 6x Kryo 470 Silver 1.8GHz  | 2x Kryo470 Gold 2.2GHz |            |
| Cortex-A55                 | Cortex-A76             |            |
| 6 PMU counters             | 6 PMU counters         |            |

-   cluster

| Cortex-A55  | Cortex-A76  |
| ----------- | ----------- |
| cpu0 - cpu5 | cpu6 - cpu7 |
| policy0     | policy6     |
| `300000`    | `300000`    |
| 576000      | 652800      |
| 768000      | 806400      |
| 1017600     | 979200      |
| 1248000     | 1094400     |
| `1324800`   | 1209600     |
| 1497600     | `1324800`   |
| 1612800     | 1555200     |
| `1708800`   | `1708800`   |
| 1804800     | 1843200     |
|             | 1939200     |
|             | 2169600     |
|             | 2208000     |

-   governor

| governor    |
| ----------- |
| userspace   |
| powersave   |
| performance |
| schedutil   |

#### Android 12

## 環境

### git

```zsh
git config --global user.name [使用者名稱]
git config --global user.email [使用者名稱]@gmail.com
```

### repo

```zsh
mkdir -p ~/.bin

curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+rx ~/.bin/repo
```

### python3

```zsh
sudo ln -sf /usr/bin/python3 /usr/bin/python
```

### others

```zsh
sudo apt install -y git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
```

## AOSP

```zsh
mkdir aosp
cd aosp
```

### 代碼同步

-   [version](https://source.android.com/docs/setup/about/build-numbers#source-code-tags-and-builds)

```zsh
PATH="${HOME}/.bin:${PATH}"

repo init --depth=1 -u https://android.googlesource.com/platform/manifest -b android-12.1.0_r11
repo sync -c --no-tags --no-clone-bundle -j$(nproc --all)
```

### 驅動導入

-   [version](https://developers.google.com/android/drivers#sunfishsq3a.220705.003.a1)

#### Google

```zsh
wget https://dl.google.com/dl/android/aosp/google_devices-sunfish-sq3a.220705.003.a1-8cbdb344.tgz
tar xvfz google_devices-sunfish-sq3a.220705.003.a1-8cbdb344.tgz
./extract-google_devices-sunfish.sh
```

-   Click `CTRL`+`C` and then type "I ACCEPT" for the long license of shellscript

#### Qualcomm

```zsh
wget https://dl.google.com/dl/android/aosp/qcom-sunfish-sq3a.220705.003.a1-34e47090.tgz
tar xvfz qcom-sunfish-sq3a.220705.003.a1-34e47090.tgz
./extract-qcom-sunfish.sh
```

-   Click `CTRL`+`C` and then type "I ACCEPT" for the long license of shellscript

### 專案構建

```zsh
. build/envsetup.sh
lunch aosp_sunfish-userdebug

m -j$(nproc --all)
```

### 映像刷機（Android Debug Bridge）

#### 安裝

```zsh
brew install -- cask android-platform-tools # for macOS
```

#### 刷入

```zsh
export ANDROID_PRODUCT_OUT=./out/target/product/sunfish

adb reboot bootloader
fastboot flashing unlock
fastboot flashall -w
```

#### 提權

```zsh
adb root // don't need root under the path "/data/local/tmp/"
```

## Benchmark

### LMbench

-   [教學](https://github.com/misakisuna705/LMbench)

#### 刷入

```zsh
adb push lmbench-3.0-a9/bin/aarch64 /data/local/tmp/LMbench
```

### MiBench

-   [教學](https://github.com/misakisuna705/MiBench)

#### 刷入

```zsh
adb push mibench/automotive/bitcount/bitcnts /data/local/tmp/Mibench/bitcnts
```

### Dhrystone

-   [教學](https://github.com/misakisuna705/Dhrystone)

#### 刷入

```zsh
adb push dhrystone/v2.2/dry /data/local/tmp/Dhrystone/dry
```

### MediaBench（Deprecated）

-   [教學](https://github.com/misakisuna705/MediaBench)

#### H.264

##### 刷入

```zsh
adb push mediaBench/mb2_vid_h264 /data/local/tmp/MediaBench/mb2_vid_h264
```

##### 執行

```zsh

```

#### JPEG-2000

##### 刷入

```zsh
adb push mediaBench/mb2_vid_jpg2000 /data/local/tmp/MediaBench/mb2_vid_jpg2000
```

##### 執行

```zsh

```

### Geekbench（Deprecated）

-   [教學](https://github.com/misakisuna705/Geekbench)

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

### SPEC CPU® 2017

-   [教學](https://github.com/misakisuna705/SPEC-CPU-2017)

#### 刷入

```zsh
adb push speccpu2017 /data/local/tmp
```

### SPEC CPU® 2006

-   [教學](https://github.com/misakisuna705/SPEC-CPU-2006)

#### 刷入

```zsh
adb push speccpu2006 /data/local/tmp
```

## Profiler

-   [教學](doc/cpufreq.md)

### 執行

-   [Simpleperf](https://github.com/misakisuna705/Simpleperf)

```zsh
python3 profiler.py [-h] [-b BENCHMARK] [-o OUTPUTFILE]

# Mibench
python3 src/profiler.py -b "/data/local/tmp/Mibench/bitcnts 84600000" -o "bin/Mibench/bitcnts/84600000.csv"

# LMbench
python3 src/profiler.py -b "/data/local/tmp/LMbench/bw_mem 512m rd" -o "bin/LMbench/bw_mem/512m/rd.csv"
python3 src/profiler.py -b "/data/local/tmp/LMbench/bw_mem 512m frd" -o "bin/LMbench/bw_mem/512m/frd.csv"
python3 src/profiler.py -b "/data/local/tmp/LMbench/bw_mem 512m cp" -o "bin/LMbench/bw_mem/512m/cp.csv"
python3 src/profiler.py -b "/data/local/tmp/LMbench/bw_mem 512m fcp" -o "bin/LMbench/bw_mem/512m/fcp.csv"
python3 src/profiler.py -b "/data/local/tmp/LMbench/bw_mem 512m bzero" -o "bin/LMbench/bw_mem/512m/bzero.csv"
python3 src/profiler.py -b "/data/local/tmp/LMbench/bw_mem 512m bcopy" -o "bin/LMbench/bw_mem/512m/bcopy.csv"

# Dhrystone
python3 src/profiler.py -b "/data/local/tmp/Dhrystone/dry" -o "bin/Dhrystone/dry.csv"

# SPEC CPU® 2017

## 600.perlbench_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/600.perlbench_s/run_base_test_mytest-64.0000/600.perlbench_s.sh" -o "bin/SpecCpu2017/600.perlbench_s.csv"

## 602.gcc_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/602.gcc_s/run_base_test_mytest-64.0000/602.gcc_s.sh" -o "bin/SpecCpu2017/602.gcc_s.csv"

## 605.mcf_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/605.mcf_s/run_base_test_mytest-64.0000/605.mcf_s.sh" -o "bin/SpecCpu2017/605.mcf_s.csv"

## 619.lbm_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/619.lbm_s/run_base_test_mytest-64.0000/619.lbm_s.sh" -o "bin/SpecCpu2017/619.lbm_s.csv"

## 620.omnetpp_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/620.omnetpp_s/run_base_test_mytest-64.0000/620.omnetpp_s.sh" -o "bin/SpecCpu2017/620.omnetpp_s.csv"

## 623.xalancbmk_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/623.xalancbmk_s/run_base_test_mytest-64.0000/623.xalancbmk_s.sh" -o "bin/SpecCpu2017/623.xalancbmk_s.csv"

## 625.x264_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/625.x264_s/run_base_test_mytest-64.0000/625.x264_s.sh" -o "bin/SpecCpu2017/625.x264_s.csv"

## 631.deepsjeng_s (Deprecated)
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/631.deepsjeng_s/run_base_test_mytest-64.0000/631.deepsjeng_s.sh" -o "bin/SpecCpu2017/631.deepsjeng_s.csv"

## 638.imagick_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/638.imagick_s/run_base_test_mytest-64.0000/638.imagick_s.sh" -o "bin/SpecCpu2017/638.imagick_s.csv"

## 641.leela_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/641.leela_s/run_base_test_mytest-64.0000/641.leela_s.sh" -o "bin/SpecCpu2017/641.leela_s.csv"

## 644.nab_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/644.nab_s/run_base_test_mytest-64.0000/644.nab_s.sh" -o "bin/SpecCpu2017/644.nab_s.csv"

## 657.xz_s
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2017/657.xz_s/run_base_test_mytest-64.0000/657.xz_s.sh" -o "bin/SpecCpu2017/657.xz_s.csv"

# SPEC CPU® 2006

## 400.perlbench
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/400.perlbench/run_base_test_lnx64-gcc.0000/400.perlbench.sh" -o "bin/SpecCpu2006/400.perlbench.csv"

## 401.bzip2
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/401.bzip2/run_base_test_lnx64-gcc.0000/401.bzip2.sh" -o "bin/SpecCpu2006/401.bzip2.csv"

## 403.gcc
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/403.gcc/run_base_test_lnx64-gcc.0000/403.gcc.sh" -o "bin/SpecCpu2006/403.gcc.csv"

## 429.mcf
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/429.mcf/run_base_test_lnx64-gcc.0000/429.mcf.sh" -o "bin/SpecCpu2006/429.mcf.csv"

## 433.milc
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/433.milc/run_base_test_lnx64-gcc.0000/433.milc.sh" -o "bin/SpecCpu2006/433.milc.csv"

## 444.namd
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/444.namd/run_base_test_lnx64-gcc.0000/444.namd.sh" -o "bin/SpecCpu2006/444.namd.csv"

## 445.gobmk
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/445.gobmk/run_base_test_lnx64-gcc.0000/445.gobmk.sh" -o "bin/SpecCpu2006/445.gobmk.csv"

## 447.dealII
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/447.dealII/run_base_test_lnx64-gcc.0000/447.dealII.sh" -o "bin/SpecCpu2006/447.dealII.csv"

## 450.soplex
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/450.soplex/run_base_test_lnx64-gcc.0000/450.soplex.sh" -o "bin/SpecCpu2006/450.soplex.csv"

## 453.povray
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/453.povray/run_base_test_lnx64-gcc.0000/453.povray.sh" -o "bin/SpecCpu2006/453.povray.csv"

## 456.hmmer
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/456.hmmer/run_base_test_lnx64-gcc.0000/456.hmmer.sh" -o "bin/SpecCpu2006/456.hmmer.csv"

## 458.sjeng
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/458.sjeng/run_base_test_lnx64-gcc.0000/458.sjeng.sh" -o "bin/SpecCpu2006/458.sjeng.csv"

## 462.libquantum
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/462.libquantum/run_base_test_lnx64-gcc.0000/462.libquantum.sh" -o "bin/SpecCpu2006/462.libquantum.csv"

## 464.h264ref
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/464.h264ref/run_base_test_lnx64-gcc.0000/464.h264ref.sh" -o "bin/SpecCpu2006/464.h264ref.csv"

## 470.lbm
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/470.lbm/run_base_test_lnx64-gcc.0000/470.lbm.sh" -o "bin/SpecCpu2006/470.lbm.csv"

## 471.omnetpp
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/471.omnetpp/run_base_test_lnx64-gcc.0000/471.omnetpp.sh" -o "bin/SpecCpu2006/471.omnetpp.csv"

## 473.astar
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/473.astar/run_base_test_lnx64-gcc.0000/473.astar.sh" -o "bin/SpecCpu2006/473.astar.csv"

## 482.sphinx3
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/482.sphinx3/run_base_test_lnx64-gcc.0000/482.sphinx3.sh" -o "bin/SpecCpu2006/482.sphinx3.csv"

## 483.xalancbmk
python3 src/profiler.py -b "/data/local/tmp/SpecCpu2006/483.xalancbmk/run_base_test_lnx64-gcc.0000/483.xalancbmk.sh" -o "bin/SpecCpu2006/483.xalancbmk.csv"
```

## info

### paper

-   [Run-Time CPU Power Modelling](http://www.powmon.ecs.soton.ac.uk/powermodeling/index.html)

### doc

-   [使用 Batterystats 和 Battery Historian 剖析電池用量](https://developer.android.com/topic/performance/power/setup-battery-historian)
-   [Android 分析器](https://developer.android.com/studio/profile/android-profiler?hl=zh-tw)
-   [使用能源分析器檢查能源用量](https://developer.android.com/studio/profile/energy-profiler)

### stackoverflow

-   [How to change clock frequency in Android?](https://stackoverflow.com/questions/4238959/how-to-change-clock-frequency-in-android)
