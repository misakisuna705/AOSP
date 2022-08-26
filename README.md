# Android Open Source Project

<!-- vim-markdown-toc GFM -->

* [參數](#參數)
    - [硬體](#硬體)
    - [系統](#系統)
    - [目標](#目標)
* [環境](#環境)
    - [git](#git)
    - [repo](#repo)
    - [python3](#python3)
    - [others](#others)
* [asop](#asop)
    - [代碼同步](#代碼同步)
    - [驅動導入](#驅動導入)
        + [Google](#google)
        + [Qualcomm](#qualcomm)
    - [專案建構](#專案建構)

<!-- vim-markdown-toc -->

---

## 參數

### 硬體

-   AMD Ryzen 5 3500X
-   Micron Crucial Ballistix Sport LT DDR4 3200（48G）
-   ADATA XPG SX8200Pro（512G）

### 系統

-   Windows 11
-   Ubuntu 18.04（WSL）

### 目標

-   Pixel 4
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
PATH="${HOME}/.bin:${PATH}"
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

## asop

```zsh
mkdir aosp
cd aosp
```

### 代碼同步

```zsh
repo init --depth=1 -u https://android.googlesource.com/platform/manifest -b android-12.1.0_r11
repo sync -c --no-tags --no-clone-bundle -j$(nproc --all)
```

### 驅動導入

#### Google

```zsh
wget https://dl.google.com/dl/android/aosp/google_devices-flame-sq3a.220705.003.a1-f7055a83.tgz
tar xvfz google_devices-flame-sq3a.220705.003.a1-f7055a83.tgz
./extract-google_devices-flame.sh
```

#### Qualcomm

```zsh
wget https://dl.google.com/dl/android/aosp/qcom-flame-sq3a.220705.003.a1-f11cbfb0.tgz
tar xvfz qcom-flame-sq3a.220705.003.a1-f11cbfb0.tgz
./extract-qcom-flame.sh
```

### 專案建構

```zsh
. build/envsetup.sh
lunch aosp_flame-userdebug
m -j$(nproc --all)
```
