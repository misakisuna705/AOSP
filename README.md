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
        + [執行](#執行)
    - [MiBench](#mibench)
        + [構建](#構建-1)
        + [刷入](#刷入-2)
        + [執行](#執行-1)
* [Analysis](#analysis)
    - [Simpleperf](#simpleperf)
        + [LMbench](#lmbench-1)
        + [Mibench](#mibench-1)
* [info](#info)
    - [sys](#sys)
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
-   2x Kryo470 Gold 2.2GHz 256KB L2（Cortex-A76）
-   6x Kryo470 Silver 1.8GHz 128KB L2（Cortex-A55）
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
simpleperf list

List of pmu events:
  arm_dsu_0/bus_access/
  arm_dsu_0/bus_cycles/
  arm_dsu_0/cycles/
  arm_dsu_0/l3d_cache/
  arm_dsu_0/l3d_cache_allocate/
  arm_dsu_0/l3d_cache_refill/
  arm_dsu_0/l3d_cache_wb/
  arm_dsu_0/memory_error/
  armv8_pmuv3/br_mis_pred/
  armv8_pmuv3/br_mis_pred_retired/
  armv8_pmuv3/br_pred/
  armv8_pmuv3/br_retired/


  armv8_pmuv3/bus_access/ # Accurate and Stable Run-Time Power Modeling for Mobile and Embedded CPUs - STAGE 1 - 0X11 - BUS_ACCESS


  armv8_pmuv3/bus_cycles/
  armv8_pmuv3/cid_write_retired/


  armv8_pmuv3/cpu_cycles/ # Accurate and Stable Run-Time Power Modeling for Mobile and Embedded CPUs - STAGE 1 - 0X11 - CYCLE_COUNT


  armv8_pmuv3/exc_return/
  armv8_pmuv3/exc_taken/
  armv8_pmuv3/inst_retired/


  armv8_pmuv3/inst_spec/ # Accurate and Stable Run-Time Power Modeling for Mobile and Embedded CPUs - STAGE 1 - 0X1B - INST_SPEC


  armv8_pmuv3/l1d_cache/
  armv8_pmuv3/l1d_cache_refill/
  armv8_pmuv3/l1d_cache_wb/
  armv8_pmuv3/l1d_tlb/
  armv8_pmuv3/l1d_tlb_refill/
  armv8_pmuv3/l1i_cache/
  armv8_pmuv3/l1i_cache_refill/
  armv8_pmuv3/l1i_tlb/
  armv8_pmuv3/l1i_tlb_refill/
  armv8_pmuv3/l2d_cache/
  armv8_pmuv3/l2d_cache_allocate/
  armv8_pmuv3/l2d_cache_refill/
  armv8_pmuv3/l2d_cache_wb/
  armv8_pmuv3/l2d_tlb/
  armv8_pmuv3/l2d_tlb_refill/
  armv8_pmuv3/l3d_cache/
  armv8_pmuv3/l3d_cache_allocate/
  armv8_pmuv3/l3d_cache_refill/
  armv8_pmuv3/l3d_cache_wb/
  armv8_pmuv3/mem_access/
  armv8_pmuv3/memory_error/
  armv8_pmuv3/stall_backend/
  armv8_pmuv3/stall_frontend/
  armv8_pmuv3/sw_incr/
  armv8_pmuv3/ttbr_write_retired/

List of raw events provided by cpu pmu:
  # Please refer to "PMU common architectural and microarchitectural event numbers"
  # and "ARM recommendations for IMPLEMENTATION DEFINED event numbers" listed in
  # ARMv8 manual for details.
  # A possible link is https://developer.arm.com/docs/ddi0487/latest/arm-architecture-reference-manual-armv8-for-armv8-a-architecture-profile.
  raw-ase-spec		# Operation speculatively executed, Advanced SIMD instruction
  raw-br-immed-retired (may not supported)		# Instruction architecturally executed, immediate branch
  raw-br-immed-spec		# Branch speculatively executed, immediate branch
  raw-br-indirect-spec		# Branch speculatively executed, indirect branch
  raw-br-mis-pred		# Mispredicted or not predicted branch Speculatively executed
  raw-br-mis-pred-retired		# Instruction architecturally executed, mispredicted branch
  raw-br-pred		# Predictable branch Speculatively executed
  raw-br-retired		# Instruction architecturally executed, branch
  raw-br-return-retired (may not supported)		# Instruction architecturally executed, Condition code check pass, procedure return
  raw-br-return-spec		# Branch speculatively executed, procedure return
  raw-bus-access		# Bus access
  raw-bus-access-normal (may not supported)		# Bus access, normal
  raw-bus-access-not-shared (may not supported)		# Bus access, not Normal, Cacheable, Shareable
  raw-bus-access-periph (may not supported)		# Bus access, peripheral
  raw-bus-access-rd		# Bus access, read
  raw-bus-access-shared (may not supported)		# Bus access, Normal, Cacheable, Shareable
  raw-bus-access-wr		# Bus access, write
  raw-bus-cycles		# Bus cycle
  raw-chain (may not supported)		# For odd-numbered counters, increments the count by one for each overflow of the preceding even-numbered counter. For even-numbered counters, there is no increment.
  raw-cid-write-retired (may not supported)		# Instruction architecturally executed, Condition code check pass, write to CONTEXTIDR
  raw-cnt-cycles (may not supported)		# Constant frequency cycles
  raw-cpu-cycles		# Cycle
  raw-crypto-spec		# Operation speculatively executed, Cryptographic instruction
  raw-dmb-spec		# Barrier speculatively executed, DMB


  raw-dp-spec		# Operation speculatively executed, integer data processing # Accurate and Stable Run-Time Power Modeling for Mobile and Embedded CPUs - STAGE 1 - DP_SPEC


  raw-dsb-spec (may not supported)		# Barrier speculatively executed, DSB
  raw-dtlb-walk		# Attributable data or unified TLB access with at least one translation table walk
  raw-exc-dabort (may not supported)		# Exception taken, Data Abort and SError
  raw-exc-fiq (may not supported)		# Exception taken, FIQ
  raw-exc-hvc (may not supported)		# Exception taken, Hypervisor Call
  raw-exc-irq (may not supported)		# Exception taken, IRQ
  raw-exc-pabort (may not supported)		# Exception taken, Instruction Abort
  raw-exc-return		# Instruction architecturally executed, Condition code check pass, exception return
  raw-exc-smc (may not supported)		# Exception taken, Secure Monitor Call
  raw-exc-svc		# Exception taken, Supervisor Call
  raw-exc-taken		# Exception taken
  raw-exc-trap-dabort (may not supported)		# Exception taken, Data Abort or SError not Taken locallyb
  raw-exc-trap-fiq (may not supported)		# Exception taken, FIQ not Taken locallyb
  raw-exc-trap-irq (may not supported)		# Exception taken, IRQ not Taken locallyb
  raw-exc-trap-other (may not supported)		# Exception taken, Other traps not Taken locallyb
  raw-exc-trap-pabort (may not supported)		# Exception taken, Instruction Abort not Taken locallyb
  raw-exc-undef (may not supported)		# Exception taken, Other synchronous
  raw-inst-retired		# Instruction architecturally executed
  raw-inst-spec		# Operation Speculatively executed
  raw-isb-spec		# Barrier speculatively executed, ISB
  raw-itlb-walk (may not supported)		# Attributable instruction TLB access with at least one translation table walk
  raw-l1d-cache		# Level 1 data cache access
  raw-l1d-cache-allocate (may not supported)		# Attributable Level 1 data cache allocation without refill
  raw-l1d-cache-inval (may not supported)		# Attributable Level 1 data cache invalidate
  raw-l1d-cache-lmiss-rd (may not supported)		# Level 1 data cache long-latency read miss
  raw-l1d-cache-rd		# Level 1 data cache read
  raw-l1d-cache-refill		# Level 1 data cache refill
  raw-l1d-cache-refill-inner		# Attributable Level 1 data cache refill, inner
  raw-l1d-cache-refill-outer		# Attributable Level 1 data cache refill, outer
  raw-l1d-cache-refill-rd		# Attributable Level 1 data cache refill, read
  raw-l1d-cache-refill-wr		# Attributable Level 1 data cache refill, write
  raw-l1d-cache-wb		# Attributable Level 1 data cache write-back
  raw-l1d-cache-wb-clean (may not supported)		# Level 1 data cache Write-Back, cleaning and coherency
  raw-l1d-cache-wb-victim		# Attributable Level 1 data cache Write-Back, victim
  raw-l1d-cache-wr		# Attributable Level 1 data cache access, write
  raw-l1d-tlb		# Attributable Level 1 data or unified TLB access
  raw-l1d-tlb-rd		# Attributable Level 1 data or unified TLB access, read
  raw-l1d-tlb-refill		# Attributable Level 1 data TLB refill
  raw-l1d-tlb-refill-rd		# Attributable Level 1 data TLB refill, read
  raw-l1d-tlb-refill-wr		# Attributable Level 1 data TLB refill, write
  raw-l1d-tlb-wr		# Attributable Level 1 data or unified TLB access, write


  raw-l1i-cache		# Attributable Level 1 instruction cache access # Accurate and Stable Run-Time Power Modeling for Mobile and Embedded CPUs - STAGE 1 - L1I_CACHE_ACCESS


  raw-l1i-cache-lmiss (may not supported)		# Level 1 instruction cache long-latency miss
  raw-l1i-cache-refill		# Level 1 instruction cache refill
  raw-l1i-tlb		# Attributable Level 1 instruction TLB access
  raw-l1i-tlb-refill		# Attributable Level 1 instruction TLB refill
  raw-l2d-cache		# Level 2 data cache access
  raw-l2d-cache-allocate		# Attributable Level 2 data cache allocation without refill
  raw-l2d-cache-inval (may not supported)		# Attributable Level 2 data cache invalidate
  raw-l2d-cache-lmiss-rd (may not supported)		# Level 2 data cache long-latency read miss


  raw-l2d-cache-rd		# Attributable Level 2 data cache access, read # Accurate and Stable Run-Time Power Modeling for Mobile and Embedded CPUs - STAGE 1 - L2D_CACHE_LD


  raw-l2d-cache-refill		# Level 2 data cache refill
  raw-l2d-cache-refill-rd		# Attributable Level 2 data cache refill, read
  raw-l2d-cache-refill-wr (may not supported)		# Attributable Level 2 data cache refill, write
  raw-l2d-cache-wb		# Attributable Level 2 data cache write-back
  raw-l2d-cache-wb-clean (may not supported)		# Level 2 data cache Write-Back, cleaning and coherency
  raw-l2d-cache-wb-victim		# Attributable Level 2 data cache Write-Back, victim
  raw-l2d-cache-wr		# Attributable Level 2 data cache access, write
  raw-l2d-tlb		# Attributable Level 2 data or unified TLB access
  raw-l2d-tlb-rd		# Attributable Level 2 data or unified TLB access, read
  raw-l2d-tlb-refill (may not supported)		# Attributable Level 2 data or unified TLB refill
  raw-l2d-tlb-refill-rd (may not supported)		# Attributable Level 2 data or unified TLB refill, read
  raw-l2d-tlb-refill-wr (may not supported)		# Attributable Level 2 data or unified TLB refill, write
  raw-l2d-tlb-wr		# Attributable Level 2 data or unified TLB access, write
  raw-l2i-cache (may not supported)		# Attributable Level 2 instruction cache access
  raw-l2i-cache-lmiss (may not supported)		# Level 2 instruction cache long-latency miss
  raw-l2i-cache-refill (may not supported)		# Attributable Level 2 instruction cache refill
  raw-l2i-tlb (may not supported)		# Attributable Level 2 instruction TLB access
  raw-l2i-tlb-refill (may not supported)		# Attributable Level 2 instruction TLB refill
  raw-l3d-cache		# Attributable Level 3 data cache access
  raw-l3d-cache-allocate		# Attributable Level 3 data or unified cache allocation without refill
  raw-l3d-cache-inval (may not supported)		# Attributable Level 3 data or unified cache access, invalidate
  raw-l3d-cache-lmiss-rd (may not supported)		# Level 3 data cache long-latency read miss
  raw-l3d-cache-rd		# Attributable Level 3 data or unified cache access, read
  raw-l3d-cache-refill		# Attributable Level 3 data cache refill
  raw-l3d-cache-refill-rd (may not supported)		# Attributable Level 3 data or unified cache refill, read
  raw-l3d-cache-refill-wr (may not supported)		# Attributable Level 3 data or unified cache refill, write
  raw-l3d-cache-wb (may not supported)		# Attributable Level 3 data or unified cache write-back
  raw-l3d-cache-wb-clean (may not supported)		# Attributable Level 3 data or unified cache Write-Back, cache clean
  raw-l3d-cache-wb-victim (may not supported)		# Attributable Level 3 data or unified cache Write-Back, victim
  raw-l3d-cache-wr (may not supported)		# Attributable Level 3 data or unified cache access, write
  raw-ld-retired (may not supported)		# Instruction architecturally executed, Condition code check pass, load
  raw-ld-spec		# Operation speculatively executed, load
  raw-ldrex-spec		# Exclusive operation speculatively executed, LDREX or LDX
  raw-ldst-spec (may not supported)		# Operation speculatively executed, load or store
  raw-ll-cache (may not supported)		# Attributable Last Level data cache access
  raw-ll-cache-miss (may not supported)		# Attributable Last level data or unified cache miss
  raw-ll-cache-miss-rd		# Attributable Last Level cache memory read miss
  raw-ll-cache-rd		# Attributable Last Level cache memory read
  raw-mem-access		# Data memory access
  raw-mem-access-rd		# Data memory access, read
  raw-mem-access-wr		# Data memory access, write
  raw-memory-error (may not supported)		# Local memory error
  raw-op-retired (may not supported)		# Micro-operation architecturally executed
  raw-op-spec (may not supported)		# Micro-operation Speculatively executed
  raw-pc-write-retired (may not supported)		# Instruction architecturally executed, Condition code check pass, software change of the PC
  raw-pc-write-spec		# Operation speculatively executed, software change of the PC
  raw-rc-ld-spec		# Release consistency operation speculatively executed, Load-Acquire
  raw-rc-st-spec		# Release consistency operation speculatively executed, Store-Release
  raw-remote-access (may not supported)		# Attributable access to another socket in a multi-socket system
  raw-remote-access-rd (may not supported)		# Attributable memory read access to another socket in a multi-socket system
  raw-sample-collision (may not supported)		# Sample collided with previous sample
  raw-sample-feed (may not supported)		# Sample Taken
  raw-sample-filtrate (may not supported)		# Sample Taken and not removed by filtering
  raw-sample-pop (may not supported)		# Sample Population
  raw-st-retired (may not supported)		# Instruction architecturally executed, Condition code check pass, store
  raw-st-spec		# Operation speculatively executed, store
  raw-stall (may not supported)		# No operation sent for execution
  raw-stall-backend		# No operation issued due to backend
  raw-stall-backend-mem (may not supported)		# Memory stall cycles
  raw-stall-frontend		# No operation issued due to the frontend
  raw-stall-slot (may not supported)		# No operation sent for execution on a Slot
  raw-stall-slot-backend (may not supported)		# No operation sent for execution on a Slot due to the backend
  raw-stall-slot-frontend (may not supported)		# No operation send for execution on a Slot due to the frontend
  raw-strex-fail-spec (may not supported)		# Exclusive operation speculatively executed, STREX or STX fail
  raw-strex-pass-spec		# Exclusive operation speculatively executed, STREX or STX pass
  raw-strex-spec		# Exclusive operation speculatively executed, STREX or STX
  raw-sve-inst-retired		# SVE Instructions architecturally executed
  raw-sve-inst-spec (may not supported)		# SVE Instructions speculatively executed
  raw-sw-incr (may not supported)		# Instruction architecturally executed, Condition code check pass, software increment
  raw-ttbr-write-retired (may not supported)		# Instruction architecturally executed, Condition code check pass, write to TTBR
  raw-unaligned-ld-spec		# Unaligned access, read
  raw-unaligned-ldst-retired (may not supported)		# Instruction architecturally executed, Condition code check pass, unaligned load or store


  raw-unaligned-ldst-spec		# Unaligned access # Accurate and Stable Run-Time Power Modeling for Mobile and Embedded CPUs - STAGE 1 - UNALIGNED_LDST_SPEC


  raw-unaligned-st-spec		# Unaligned access, write
  raw-vfp-spec (may not supported)		# Operation speculatively executed, floating-point instruction
```

#### LMbench

#### Mibench

```zsh
adb shell simpleperf stat --use-devfreq-counters --per-core /data/local/tmp/Mibench/bitcnts [圈數]
adb shell simpleperf stat --use-devfreq-counters --per-core --interval 100 /data/local/tmp/Mibench/bitcnts [圈數]
```

## info

### sys

```zsh
# get frequency
adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq

# get voltage
adb shell cat /sys/class/power_supply/battery/voltage_now

# get available DVFS Governor
adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors

# set DVFS governor manual mode
adb shell echo "userspace" > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

# set frequency
adb shell su -c "echo "[頻率（KHz）]" > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed"

# set core disable
adb shell su -c "stop mpdecision"
adb reboot
adb shell su -c "echo "0" > /sys/devices/system/cpu/cpu3/online"
```

### doc

-   [使用 Batterystats 和 Battery Historian 剖析電池用量](https://developer.android.com/topic/performance/power/setup-battery-historian)
-   [Android 分析器](https://developer.android.com/studio/profile/android-profiler?hl=zh-tw)
-   [使用能源分析器檢查能源用量](https://developer.android.com/studio/profile/energy-profiler)

### stackoverflow

-   [How to change clock frequency in Android?](https://stackoverflow.com/questions/4238959/how-to-change-clock-frequency-in-android)
