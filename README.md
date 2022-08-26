<!-- vim-markdown-toc GFM -->

+ [a](#a)

<!-- vim-markdown-toc -->

---

# a

```powershel
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```


Windows

    PowerShell

    	#檢視OpenSSH狀態與版本

    	Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

    	#安裝ssh server

    	Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

    	#設定開機自動啓動ssh server

    	Get-Service -Name sshd | Set-Service -StartupType Auto

    	#啟用WSL

    	dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

    	#啟用虛擬機

    	dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

    	#更新WSL元件

    	https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

    	#啟用WSL2

    	wsl --set-default-version 2

    	#安裝Chocolatey

    	Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

    	#安裝LxRunOffline

    	choco install lxrunoffline

    	#下載Ubuntu

    	https://aka.ms/wsl-ubuntu-1804

    	#副檔名更改成zip，並解壓縮

    	/Ubuntu_1804.2019.522.0_x64

    	#安裝Ubuntu

    	LxRunOffline i -n Ubuntu -d e:\WSL\Ubuntu -f  "C:\Users\misak\Downloads\Ubuntu_1804.2019.522.0_x64\install.tar.gz" -s

    WSL

    	useradd -m -s /bin/bash misakisuna

    	passwd misakisuna

    	usermod -aG sudo misakisuna

    PowerShell

    	lxrunoffline su -n Ubuntu -v 1000

    WSL

    	sudo apt update
    	sudo apt upgrade -y
    	sudo apt dist-upgrade
    	sudo apt autoclean
    	sudo apt autoremove -y

    	sudo apt install -y openssh-server
    	/etc/ssh/sshd_config
    		PasswordAuthentication yes
    	sudo /etc/init.d/ssh start

    	curl -s https://install.zerotier.com | sudo bash
    	sudo zerotier-cli join a09acf0233b4a4b5
    	sudo zerotier-one -d

    	/etc/init.wsl
    		#！ /bin/sh
    		/etc/init.d/ssh $1
    		/etc/init.d/zerotier-one

    	sudo chmod u+x /etc/init.wsl

    Windows + R

    	shell:startup

    	Ubuntu.vbs
    		Set ws = CreateObject("Wscript.Shell")
    		ws.run "wsl -d Ubuntu -u root /etc/init.wsl start", vbhide

    WSL

    	sudo apt install -y git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig

    	sudo ln -sf /usr/bin/python3 /usr/bin/python

    	mkdir -p ~/.bin
    	PATH="${HOME}/.bin:${PATH}"
    	curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
    	chmod a+rx ~/.bin/repo

    	mkdir aosp

    	cd aosp

    		git config --global user.name misakisuna
    		git config --global user.email misakisuna705@gmail.com

    		repo init --depth=1 -u https://android.googlesource.com/platform/manifest -b android-12.1.0_r11
    		repo sync -c --no-tags --no-clone-bundle  -j$(nproc --all)

    		…

    		wget https://dl.google.com/dl/android/aosp/google_devices-flame-sq3a.220705.003.a1-f7055a83.tgz
    		tar xvfz google_devices-flame-sq3a.220705.003.a1-f7055a83.tgz
    		./extract-google_devices-flame.sh

    		wget https://dl.google.com/dl/android/aosp/qcom-flame-sq3a.220705.003.a1-f11cbfb0.tgz
    		tar xvfz qcom-flame-sq3a.220705.003.a1-f11cbfb0.tgz
    		./extract-qcom-flame.sh

    		. build/envsetup.sh
    		lunch aosp_flame-userdebug
    		m -j$(nproc --all)
