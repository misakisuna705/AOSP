# Android Open Source Project

<!-- vim-markdown-toc GFM -->

* [參數](#參數)
    - [系統](#系統)
    - [目標](#目標)
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
        + [執行](#執行)
    - [MiBench](#mibench)
        + [構建](#構建-1)
        + [刷入](#刷入-2)
        + [執行](#執行-1)
* [Analysis](#analysis)
    - [Simpleperf](#simpleperf)

<!-- vim-markdown-toc -->

---

## 參數

### 系統

-   Ubuntu 18.04（WSL）

### 目標

-   Pixel 4a
-   Android 12

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

#### 執行

```zsh
adb shell /data/local/tmp/LMbench/bw_mem 512m [執行檔]
```

### MiBench

#### 構建

-   [教學](https://github.com/misakisuna705/MiBench)

#### 刷入

```zsh
adb push mibench/automotive/bitcount/bitcnts /data/local/tmp/Mibench/bitcnts
```

#### 執行

```zsh
adb shell /data/local/tmp/Mibench/bitcnts [圈數]
```

## Analysis

### Simpleperf

```zsh
adb shell simpleperf stat --use-devfreq-counters --per-core ./[benchmark 執行檔] [benchmark 參數]
```
