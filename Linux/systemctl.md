# Linux Systemctl

守护进程

## Command

- `systemctl start ServerName`：启动服务
- `systemctl stop ServerName`：停止服务
- `systemctl restart ServerName`：重启服务
- `systemctl enable ServerName`：设置服务开机自启动
- `systemctl disable ServerName`：取消服务开机自启动
- `systemctl status ServerName`：查看服务状态
- `systemctl daemon-reload`: 重新加载配置文件
- `systemctl reload ServerName`: 重新加载配置文件

## Journalctl

- `journalctl`：查看系统日志
- `journalctl -f`：实时查看系统日志
- `journalctl -u`：查看指定服务的日志
- `journalctl --since`：查看指定时间之后的日志
- `journalctl --until`：查看指定时间之前的日志

## .service

基本的配置文件框架如下

```ini
[Unit]
Description=Description
After=network-online.target

[Service]
Uesr=root
ExecStart=/usr/bin/python3 /path/to/file.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `Description`：描述
- `After`：依赖的服务
- `User`：运行用户
- `ExecStart`：启动命令
- `Restart`：重启策略
- `WantedBy`：开机启动