# Fish

今天新配置了fish terminal，用以替代默认的bash，功能有指令补全，但是碰到一点小坑，记录一下。

## 安装

```bash
sudo apt-get install fish
```

## 设置默认shell

```bash
chsh -s /usr/bin/fish
```

在这一步出错了

我使用vscode的设置默认shell功能，由于路径错误，导致指向了一个并不存在的文件

随后使用cmd和vscode尝试ssh链接，均失败

具体表现为，原本使用公钥登录的链接，变成了使用密码登录，且输入正确密码后，仍然无法登录

## 试错

查阅资料后，使用另一账号ssh登录，查看`/etc/ssh/sshd_config`文件，根据资料修改无误后，`sudo systemctl restart sshd`, 仍然无法登录

此外，重新设置/root权限 \
`sudo chmod 700 /root`\
`sudo chmod 700 /root/.ssh`\
`sudo chmod 600 /root/.ssh/authorized_keys`\
仍然无法登录

## 解决

最后，使用`systemtcl status sshd` 发现以下Log

```bash
Aug 06 23:59:07 sea sshd[78494]: rexec line 125: Deprecated option RSAAuthentication 
Aug 06 23:59:07 sea sshd[78494]: reprocess config line 125: Deprecated option RSAAuthentication 
Aug 06 23:59:07 sea sshd[78494]: User root not allowed because shell /usr/local/bin/fish does not exist 
Aug 06 23:59:09 sea sshd[78494]: Connection reset by invalid user root 192.168.0.112 port 5308 [preauth]
```

框出重点

```bash
User root not allowed because shell /usr/local/bin/fish does not exist
```

原因是该用户的默认shell不存在，导致无法登录

使用`sudo view` 查看`/etc/passwd`文件，修改root用户的默认shell为正确路径`/usr/bin/fish`，问题解决

## 配置

在设置默认shell之前，应先进入所在文件夹进行确认，不要使用vscode的设置默认shell功能

```bash
cd /usr/bin
```

```bash
ls fish
```

```bash
chsh -s /usr/bin/fish
```

fish的配置文件默认为`~/.config/fish/config.fish`

如果使用starship，需要在配置文件中添加以下内容

```bash
nano ~/.config/fish/config.fish
vim ~/.config/fish/config.fish
```

```bash
starship init fish | source
```

需要将bash原本的配置文件移动到fish的配置文件中，否则会出现一些问题

```bash
nano ~/.bashrc
vim ~/.bashrc
```
