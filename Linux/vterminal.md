# Virtual Terminal

ssh链接Linux后，当ssh断开时，程序会自动退出，这时可以使用虚拟终端来运行程序，虚拟终端不会因为ssh断开而退出。

## Screen

### install

```bash
sudo apt-get install screen
```

### command

- `screen`：创建一个新的虚拟终端
- `screen -ls`：查看当前所有的虚拟终端
- `screen -r 虚拟终端名称`：连接到指定的虚拟终端
- `screen -d 虚拟终端名称`：断开指定的虚拟终端
- `screen -X -S 虚拟终端名称 quit`：关闭指定的虚拟终端
- `screen -wipe`：清除所有已经断开的虚拟终端
- `screen -S 虚拟终端名称`：创建一个新的虚拟终端
- `screen -S 虚拟终端名称 -X stuff "命令"`：在指定的虚拟终端中执行指定的命令

### contorl

- `Ctrl + a`：激活控制台

`以下操作需要在激活控制台后执行`

- `Ctrl + a + d`：挂起当前虚拟终端
- `Ctrl + a + c`：创建一个新的虚拟终端
- `Ctrl + a + n`：切换到下一个虚拟终端
- `Ctrl + a + p`：切换到上一个虚拟终端
- `Ctrl + a + "虚拟终端编号"`：切换到指定编号的虚拟终端
- `Ctrl + a + k`：杀掉当前虚拟终端
- `Ctrl + a + ?`：显示所有快捷键

## Tmux

### install

```bash
sudo apt-get install tmux
```

### command

- `tmux`：创建一个新的虚拟终端
- `tmux ls`：查看当前所有的虚拟终端
- `tmux attach -t 虚拟终端名称`：连接到指定的虚拟终端
- `tmux detach -t 虚拟终端名称`：断开指定的虚拟终端
- `tmux kill-session -t 虚拟终端名称`：关闭指定的虚拟终端
- `tmux kill-server`：清除所有已经断开的虚拟终端
- `tmux new -s 虚拟终端名称`：创建一个新的虚拟终端
- `tmux send -t 虚拟终端名称 "命令"`：在指定的虚拟终端中执行指定的命令

### contorl

- `Ctrl + b`：激活控制台

`以下操作需要在激活控制台后执行`

- `Ctrl + b + d`：挂起当前终端
- `Ctrl + b + c`：创建一个新的虚拟终端
- `Ctrl + b + n`：切换到下一个虚拟终端
- `Ctrl + b + p`：切换到上一个虚拟终端
- `Ctrl + b + "虚拟终端编号"`：切换到指定编号的虚拟终端
- `Ctrl + b + x`：杀掉当前虚拟终端
- `Ctrl + b + ?`：显示所有快捷键