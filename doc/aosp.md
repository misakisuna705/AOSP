# AOSP

<!-- vim-markdown-toc GFM -->

* [Pixel 4a](#pixel-4a)
    - [代碼同步](#代碼同步)
    - [驅動導入](#驅動導入)
        + [Google](#google)
        + [Qualcomm](#qualcomm)
    - [專案構建](#專案構建)
    - [映像刷機（Android Debug Bridge）](#映像刷機android-debug-bridge)
        + [安裝](#安裝)
        + [刷入](#刷入)
        + [提權](#提權)

<!-- vim-markdown-toc -->

---

## Pixel 4a

-   [CpuFreq](doc/cpufreq.md)

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
