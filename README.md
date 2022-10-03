# Android Open Source Project

<!-- vim-markdown-toc GFM -->

* [參數](#參數)
    - [系統](#系統)
    - [目標](#目標)
        + [Pixel 4a](#pixel-4a)
            * [CPU](#cpu)
            * [GPU](#gpu)
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
        + [構建](#構建)
        + [刷入](#刷入-1)
    - [MiBench](#mibench)
        + [構建](#構建-1)
        + [刷入](#刷入-2)
* [Analysis](#analysis)
    - [查詢](#查詢)
        + [頻率](#頻率)
        + [策略](#策略)
    - [設定](#設定)
        + [定核](#定核)
        + [定頻](#定頻)
        + [定策略](#定策略)
    - [執行](#執行)
    - [voltage（不要看）](#voltage不要看)
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

#### Pixel 4a

##### CPU

-   Qualcomm® Snapdragon™ 730G（Octa-core）
-   2x Kryo470 Gold 2.2GHz 256KB L2（Cortex-A76 with 6 PMU counters）
-   6x Kryo470 Silver 1.8GHz 128KB L2（Cortex-A55 with 6 PMU counters）
-   1MB L3
-   ARMv8

##### GPU

-   Adreno 618

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

#### 構建

-   [教學](https://github.com/misakisuna705/LMbench)

#### 刷入

```zsh
adb push lmbench-3.0-a9/bin/aarch64 /data/local/tmp/LMbench
```

### MiBench

#### 構建

-   [教學](https://github.com/misakisuna705/MiBench)

#### 刷入

```zsh
adb push mibench/automotive/bitcount/bitcnts /data/local/tmp/Mibench/bitcnts
```

## Analysis

### 查詢

#### 頻率

| Cortex-A55  | Cortex-A76  |     |
| ----------- | ----------- | --- |
| cpu0 - cpu5 | cpu6 - cpu7 |     |
| policy0     | policy6     |     |
| `300000`    | `300000`    |     |
| 576000      | 652800      |     |
| 768000      | 806400      |     |
| 1017600     | 979200      |     |
| 1248000     | 1094400     |     |
| `1324800`   | 1209600     |     |
| 1497600     | `1324800`   |     |
| 1612800     | 1555200     |     |
| `1708800`   | `1708800`   |     |
| 1804800     | 1843200     |     |
|             | 1939200     |     |
|             | 2169600     |     |
|             | 2208000     |     |

```zsh
adb shell "ls /sys/devices/system/cpu/cpufreq" # 查看所有可用定頻策略
adb shell "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_frequencies" # 查看所有核心頻率配置
```

```zsh
adb shell "cat /sys/devices/system/cpu/cpufreq/policy*/scaling_cur_freq" # 查看策略當前頻率設定
adb shell "cat /sys/devices/system/cpu/cpufreq/policy*/scaling_max_freq" # 查看策略最大頻率設定
adb shell "cat /sys/devices/system/cpu/cpufreq/policy*/scaling_min_freq" # 查看策略最小頻率設定
```

```zsh
adb shell "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq" # 查看核心當前頻率設定
adb shell "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq" # 查看核心最大頻率設定
adb shell "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_min_freq" # 查看核心最小頻率設定
```

#### 策略

```zsh
adb shell "cat /sys/devices/system/cpu/cpufreq/policy*/scaling_governor" # 查看策略當前 governor
```

```zsh
adb shell "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors" # 查看核心可用 governor
```

### 設定

#### 定核

```zsh
adb shell "taskset [16 進位 one hot] [benchmark]"
```

#### 定頻

```zsh
adb shell "echo 0 > /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"
adb shell "echo 99999999 > /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"
adb shell "echo schedutil > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"
adb shell "echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"
adb shell "echo [頻率] > /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"
adb shell "echo [頻率] > /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"
```

#### 定策略

```zsh
adb shell "echo [可用的governor 策略] > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"
adb shell "echo [可用的governor 策略] > /sys/devices/system/cpu/cpufreq/policy6/scaling_governor"
```

### 執行

-   [Profiler](https://github.com/misakisuna705/AOSP/blob/main/profiler.py)

```zsh
python3 profiler.py
```

### voltage（不要看）

```zsh
# get voltage
adb shell cat /sys/class/power_supply/battery/voltage_now

# get available DVFS Governor
adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors

# set DVFS governor manual mode
adb shell echo "userspace" > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

# set frequency
adb shell -c "echo "[頻率（KHz）]" > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed"

# set core disable
adb shell su -c "stop mpdecision"
adb reboot
adb shell su -c "echo "0" > /sys/devices/system/cpu/cpu3/online"
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
