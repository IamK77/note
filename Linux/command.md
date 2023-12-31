# Linux command

### 1.1 文件操作

#### 1.1.1 文件操作

- `ls`：列出目录下的文件
- `ls -l`：列出目录下的文件，显示文件的详细信息
- `ls -a`：列出目录下的文件，包括隐藏文件
- `ls -al`：列出目录下的文件，包括隐藏文件，显示文件的详细信息
- `ls -lh`：列出目录下的文件，显示文件的详细信息，文件大小以人类可读的方式显示
- `ls -R`：列出目录下的文件，包括子目录下的文件
- `ls -t`：列出目录下的文件，按照修改时间排序
- `ls -S`：列出目录下的文件，按照文件大小排序
- `ls -r`：列出目录下的文件，按照字母逆序排序
- `ls -h`：列出目录下的文件，显示文件的详细信息，文件大小以人类可读的方式显示
- `ls -lS`：列出目录下的文件，显示文件的详细信息，按照文件大小排序
- `ls -lSr`：列出目录下的文件，显示文件的详细信息，按照文件大小逆序排序

#### 1.1.2 文件操作

- `touch`：创建文件
- `touch -t`：创建文件，指定文件的修改时间
- `touch -a`：创建文件，指定文件的访问时间
- `touch -c`：创建文件，如果文件不存在，则不创建
- `touch -m`：创建文件，指定文件的修改时间
- `touch -r`：创建文件，指定文件的修改时间
- `touch -d`：创建文件，指定文件的修改时间
- `touch -t`：创建文件，指定文件的修改时间

#### 1.1.3 文件操作

- `cp`：复制文件
- `cp -r`：复制文件夹
- `cp -i`：复制文件，如果文件已经存在，则提示是否覆盖
- `cp -f`：复制文件，如果文件已经存在，则覆盖
- `cp -n`：复制文件，如果文件已经存在，则不覆盖
- `cp -u`：复制文件，如果文件已经存在，且源文件的修改时间比目标文件的修改时间新，则覆盖
- `cp -l`：复制文件，如果文件已经存在，则创建一个硬链接
- `cp -s`：复制文件，如果文件已经存在，则创建一个软链接
- `cp -a`：复制文件，复制文件的所有者、所属组、权限、修改时间、访问时间等信息
- `cp -p`：复制文件，复制文件的权限、修改时间、访问时间等信息

#### 1.1.4 文件操作

- `mv`：移动文件
- `mv -i`：移动文件，如果文件已经存在，则提示是否覆盖
- `mv -f`：移动文件，如果文件已经存在，则覆盖
- `mv -n`：移动文件，如果文件已经存在，则不覆盖
- `mv -u`：移动文件，如果文件已经存在，且源文件的修改时间比目标文件的修改时间新，则覆盖
- `mv -l`：移动文件，如果文件已经存在，则创建一个硬链接
- `mv -s`：移动文件，如果文件已经存在，则创建一个软链接
- `mv -a`：移动文件，移动文件的所有者、所属组、权限、修改时间、访问时间等信息

#### 1.1.5 文件操作

- `rm`：删除文件
- `rm -r`：删除文件夹
- `rm -f`：删除文件，不提示
- `rm -i`：删除文件，提示
- `rm -rf`：删除文件夹，不提示

#### 1.1.6 文件操作

- `mkdir`：创建文件夹
- `mkdir -p`：创建多级文件夹
- `mkdir -m`：创建文件夹，指定文件夹的权限

#### 1.1.7 文件操作

- `cat`：查看文件内容
- `cat -n`：查看文件内容，显示行号
- `cat -b`：查看文件内容，显示非空白行的行号
- `cat -s`：查看文件内容，合并多个空白行为一个空白行
- `cat -E`：查看文件内容，显示行尾的美元符号
- `cat -T`：查看文件内容，将制表符转换为空格
- `cat -A`：查看文件内容，显示所有的控制字符

#### 1.1.8 文件操作

- `more`：分页显示文件内容
- `less`：分页显示文件内容，支持向前翻页
- `head`：查看文件的前几行
- `head -n`：查看文件的前 n 行
- `tail`：查看文件的后几行
- `tail -n`：查看文件的后 n 行

#### 1.1.9 文件操作

- `ln`：创建链接文件
- `ln -s`：创建软链接文件
- `ln -f`：创建硬链接文件，如果文件已经存在，则覆盖

### 1.2 系统操作

#### 1.2.1 系统操作

- `shutdown`：关机
- `shutdown -h`：关机
- `shutdown -r`：重启
- `shutdown -c`：取消关机或重启
- `halt`：关机
- `poweroff`：关机
- `reboot`：重启

#### 1.2.2 系统操作

- `ps`：查看进程
- `ps -ef`：查看所有进程
- `ps -aux`：查看所有进程
- `ps -u`：查看指定用户的进程
- `ps -p`：查看指定进程的信息

#### 1.2.3 系统操作

- `top`：查看系统资源占用情况
- `htop`：查看系统资源占用情况，支持交互式操作
- `free`：查看内存使用情况
- `df`：查看磁盘使用情况
- `du`：查看文件或目录的大小

#### 1.2.4 系统操作

- `uname`：查看系统信息
- `uname -a`：查看系统信息，包括内核版本、主机名、操作系统版本等
- `hostname`：查看主机名
- `hostname -i`：查看主机的 IP 地址
- `ifconfig`：查看网络接口信息
- `ping`：测试网络连通性
- `traceroute`：跟踪数据包的路由路径

#### 1.2.5 系统操作

- `date`：查看系统时间
- `date -s`：设置系统时间
- `date -d`：计算日期和时间
- `cal`：查看日历
- `uptime`：查看系统运行时间和负载

#### 1.2.6 系统操作

- `useradd`：添加用户
- `userdel`：删除用户
- `usermod`：修改用户信息
- `passwd`：修改用户密码
- `groupadd`：添加用户组
- `groupdel`：删除用户组
- `groupmod`：修改用户组信息

#### 1.2.7 系统操作

- `history`：查看历史命令
- `history -c`：清空历史命令
- `history -d`：删除指定的历史命令
- `history -a`：将当前的历史命令保存到历史命令文件中
- `history -r`：从历史命令文件中读取历史命令

#### 1.2.8 系统操作

- `sudo`：以超级用户的身份执行命令
- `su`：切换用户身份
- `su -`：切换用户身份，并切换到用户的家目录
- `chown`：修改文件的所有者和所属组
- `chgrp`：修改文件的所属组
- `chmod`：修改文件的权限

#### 1.2.9 系统操作

- `find`：查找文件
- `find -name`：按照文件名查找文件
- `find -type`：按照文件类型查找文件
- `find -size`：按照文件大小查找文件
- `find -mtime`：按照文件修改时间查找文件
- `find -exec`：对查找到的文件执行指定的命令

#### 1.2.10 系统操作

- `grep`：查找文件中的指定内容
- `grep -r`：递归查找文件中的指定内容
- `grep -i`：忽略大小写查找文件中的指定内容
- `grep -v`：查找文件中不包含指定内容的行
- `grep -n`：查找文件中包含指定内容的行，并显示行号
- `grep -c`：查找文件中包含指定内容的行的数量

#### 1.2.11 系统操作

- `tar`：打包和解包文件
- `tar -c`：打包文件
- `tar -x`：解包文件
- `tar -t`：查看打包文件的内容
- `tar -z`：使用 gzip 压缩文件
- `tar -j`：使用 bzip2 压缩文件
- `tar -v`：显示详细信息
- `tar -f`：指定打包文件的名称

#### 1.2.12 系统操作

- `zip`：打包和解包文件
- `zip -r`：打包文件
- `unzip`：解包文件
- `unzip -l`：查看打包文件的内容
- `unzip -v`：显示详细信息
- `unzip -d`：指定解包文件的目录

#### 1.2.13 系统操作

- `ssh`：远程登录
- `scp`：远程拷贝文件
- `rsync`：远程同步文件
- `wget`：下载文件
- `curl`：下载文件
#### 1.2.14 系统操作

- `ps`：查看进程信息
- `kill`：终止进程
- `killall`：终止指定名称的进程
- `nohup`：在后台运行命令
- `bg`：将进程放到后台运行
- `fg`：将进程放到前台运行

#### 1.2.15 系统操作

- `shutdown`：关机
- `reboot`：重启
- `halt`：停止系统
- `poweroff`：关闭电源

#### 1.2.16 系统操作

- `yum`：安装、升级、卸载软件包
- `yum install`：安装软件包
- `yum update`：升级软件包
- `yum remove`：卸载软件包
- `yum search`：搜索软件包
- `yum list`：列出已安装的软件包

#### 1.2.17 系统操作

- `systemctl`：管理系统服务
- `systemctl start`：启动服务
- `systemctl stop`：停止服务
- `systemctl restart`：重启服务
- `systemctl enable`：设置服务开机自启动
- `systemctl disable`：取消服务开机自启动
- `systemctl status`：查看服务状态

#### 1.2.18 系统操作

- `journalctl`：查看系统日志
- `journalctl -f`：实时查看系统日志
- `journalctl -u`：查看指定服务的日志
- `journalctl --since`：查看指定时间之后的日志
- `journalctl --until`：查看指定时间之前的日志

#### 1.2.19 系统操作

- `iptables`：管理防火墙
- `iptables -L`：查看防火墙规则
- `iptables -F`：清空防火墙规则
- `iptables -A`：添加防火墙规则
- `iptables -D`：删除防火墙规则
- `iptables-save`：保存防火墙规则
- `iptables-restore`：恢复防火墙规则

#### 1.2.20 系统操作

- `crontab`：定时执行任务
- `crontab -e`：编辑定时任务
- `crontab -l`：查看定时任务
- `crontab -r`：删除定时任务

#### 1.2.21 系统操作

- `ssh-keygen`：生成 SSH 密钥
- `ssh-copy-id`：将 SSH 公钥复制到远程主机
- `ssh-add`：将 SSH 私钥添加到 SSH 代理中
- `ssh-agent`：SSH 代理

#### 1.2.22 系统操作

- `mount`：挂载文件系统
- `umount`：卸载文件系统
- `df`：查看文件系统使用情况
- `du`：查看文件或目录的大小

#### 1.2.23 系统操作

- `awk`：文本处理工具
- `awk '{print $1}'`：打印第一列
- `awk '{print $NF}'`：打印最后一列
- `awk '/pattern/{print $0}'`：打印匹配模式的行
- `awk '{sum+=$1}END{print sum}'`：计算第一列的总和
- `awk -F':' '{print $1,$7}' /etc/passwd`：打印 /etc/passwd 文件中的用户名和默认 shell

#### 1.2.24 系统操作

- `sed`：文本处理工具
- `sed 's/old/new/g'`：替换文本中的 old 为 new
- `sed '/pattern/d'`：删除匹配模式的行
- `sed '1,5d'`：删除第一行到第五行
- `sed 's/^/#/'`：在每一行的开头添加 #
- `sed 's/$/!/'`：在每一行的结尾添加 !

#### 1.2.25 系统操作

- `cut`：提取文本中的列
- `cut -d: -f1 /etc/passwd`：提取 /etc/passwd 文件中的用户名
- `cut -c1-5`：提取每一行的前五个字符
- `cut -c5-`：提取每一行的第五个字符到结尾
- `cut -f1`：提取每一行的第一列

#### 1.2.26 系统操作

- `sort`：排序文本
- `sort -n`：按照数字大小排序
- `sort -r`：倒序排序
- `sort -u`：去重排序
- `sort -t':' -k3 /etc/passwd`：按照 /etc/passwd 文件中的第三列排序

#### 1.2.27 系统操作

- `uniq`：去重文本
- `uniq -c`：统计重复行的数量
- `uniq -d`：只显示重复行
- `uniq -u`：只显示不重复行

#### 1.2.28 系统操作

- `diff`：比较文本差异
- `diff file1 file2`：比较文件差异
- `diff -u file1 file2`：以统一的格式输出差异
- `diff -r dir1 dir2`：比较目录差异

#### 1.2.29 系统操作

- `tar`：打包和解包文件
- `tar -c`：打包文件
- `tar -x`：解包文件
- `tar -t`：查看打包文件的内容
- `tar -z`：使用 gzip 压缩文件
- `tar -j`：使用 bzip2 压缩文件
- `tar -v`：显示详细信息
- `tar -f`：指定打包文件的名称

#### 1.2.30 系统操作

- `zip`：打包和解包文件
- `zip -r`：打包文件
- `unzip`：解包文件
- `unzip -l`：查看打包文件的内容
- `unzip -v`：显示详细信息
- `unzip -d`：指定解包文件的目录

#### 1.2.31 系统操作

- `rsync`：远程同步文件
- `rsync -a`：同步文件夹
- `rsync -v`：显示详细信息
- `rsync -z`：压缩传输
- `rsync -e`：指定 SSH 端口

#### 1.2.32 系统操作

- `scp`：远程拷贝文件
- `scp file user@host:/path`：将本地文件拷贝到远程主机
- `scp user@host:/path/file .`：将远程文件拷贝到本地

#### 1.2.33 系统操作

- `wget`：下载文件
- `wget url`：下载文件
- `wget -c url`：断点续传下载
- `wget -r url`：递归下载
- `wget -p url`：下载页面的所有资源

#### 1.2.34 系统操作

- `curl`：下载文件
- `curl url`：下载文件
- `curl -O url`：将文件保存到本地
- `curl -o filename url`：将文件保存到指定文件名
- `curl -C - url`：断点续传下载
