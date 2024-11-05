# GitHub Copilot CLI 命令行工具说明

## 核心命令
- `auth`: 认证 gh 和 git 与 GitHub 的连接
- `browse`: 在浏览器中打开仓库
- `codespace`: 连接并管理 codespaces
- `gist`: 管理 gists
- `issue`: 管理 issues
- `org`: 管理组织
- `pr`: 管理 pull requests
- `project`: 使用 GitHub Projects
- `release`: 管理 releases
- `repo`: 管理仓库

## GitHub Actions 命令
- `cache`: 管理 Github Actions 缓存
- `run`: 查看 workflow 运行详情
- `workflow`: 查看 GitHub Actions workflows 详情

## 扩展命令
- `copilot`: 扩展 copilot

## 别名命令
- `co`: "pr checkout" 的别名

## 其他命令
- `alias`: 创建命令快捷方式
- `api`: 发送经过认证的 GitHub API 请求
- `completion`: 生成 shell 自动补全脚本
- `config`: 管理 gh 的配置
- `extension`: 管理 gh 扩展
- `gpg-key`: 管理 GPG 密钥
- `label`: 管理标签
- `ruleset`: 查看仓库规则集信息
- `search`: 搜索仓库、issues 和 pull requests
- `secret`: 管理 GitHub secrets
- `ssh-key`: 管理 SSH 密钥
- `status`: 打印跨仓库的相关 issues、pull requests 和通知信息
- `variable`: 管理 GitHub Actions 变量

## 帮助主题
- `actions`: 学习如何使用 GitHub Actions
- `environment`: 可以与 gh 一起使用的环境变量
- `exit-codes`: gh 使用的退出代码
- `formatting`: gh 导出的 JSON 数据的格式化选项
- `mintty`: 使用 gh 与 MinTTY 的信息
- `reference`: 所有 gh 命令的全面参考

## 标志
- `--help`: 显示命令帮助
- `--version`: 显示 gh 版本

## 示例
- `$ gh issue create`
- `$ gh repo clone cli/cli`
- `$ gh pr checkout 321`

## 学习更多
- 使用 `gh <command> <subcommand> --help` 获取命令更多信息
- 在 https://cli.github.com/manual 阅读手册