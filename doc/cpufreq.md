# cpufreq

<!-- vim-markdown-toc GFM -->

* [查詢](#查詢)
    - [電壓（Deprecated）](#電壓deprecated)
    - [頻率](#頻率)
    - [策略](#策略)
* [設定](#設定)
    - [定策略](#定策略)
    - [定頻](#定頻)
    - [定核](#定核)

<!-- vim-markdown-toc -->

---

## 查詢

### 電壓（Deprecated）

```zsh
adb shell cat /sys/class/power_supply/battery/voltage_now
```

### 頻率

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

### 策略

```zsh
adb shell "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors" # 查看核心可用 governor
```

```zsh
adb shell "cat /sys/devices/system/cpu/cpufreq/policy*/scaling_governor" # 查看策略當前 governor
```

## 設定

### 定策略

```zsh
adb shell "echo [可用的governor 策略] > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"
adb shell "echo [可用的governor 策略] > /sys/devices/system/cpu/cpufreq/policy6/scaling_governor"
```

### 定頻

```zsh
adb shell "echo 0 > /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"
adb shell "echo 99999999 > /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"
adb shell "echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"
adb shell "echo [頻率] > /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"
adb shell "echo [頻率] > /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"
```

### 定核

```zsh
adb shell "taskset [16 進位 one hot] [指令]"
```
