# Wsl

wsl是windows subsystem for linux的缩写，是微软在win10中提供的一个linux子系统，可以在win10、11中运行linux程序，并与win中文件交互。

## Install

确保你的Win版本可以运行wsl，管理员权限打开cmd

```bash
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

重启


## Install Linux

如果使用Microsoft Store安装，会自动安装到C盘，因此使用Microsoft提供的[下载地址](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-6---install-your-linux-distribution-of-choice)\
选择所需版本，下载到指定位置，将下载下来的文件后辍改为zip，打开，选择对应架构的的.appx文件，解压到指定位置，将该.appx文件后辍改为.zip，解压\
此时可以看到解压后的文件里包括一个该系统的.exe文件，例如Ubuntu.exe，双击运行，即可安装该系统，安装完成后，会提示输入用户名和密码，输入即可

## Set Default Terminal

Win10可能没有Terminal

打开Terminal，新增或设置，将命令行改为.exe文件的路径，例如`path\to\ur\*\ubuntu.exe`

也有可能已经在Terminal中自动设置了，无需再进行设置

## 怎样访问Windows文件

在wsl中，可以通过`/mnt/c`访问C盘，`/mnt/d`访问D盘，以此类推



