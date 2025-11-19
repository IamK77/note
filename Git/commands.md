# Git 常用命令

## 基础操作

```bash
git init                    # 初始化仓库
git clone <url>             # 克隆远程仓库
git add <file>              # 添加文件到暂存区
git commit -m "message"     # 提交更改
git status                  # 查看状态
git log                     # 查看提交历史
```

## 分支操作

```bash
git branch                  # 查看所有分支
git checkout -b <name>     # 创建并切换到新分支
git merge <branch>         # 合并分支
git branch -d <name>      # 删除分支
```

## 远程协作

```bash
git remote -v               # 查看远程仓库
git pull                    # 拉取并合并远程更改
git push origin <branch>    # 推送分支到远程
```

## 撤销操作

```bash
git reset --hard HEAD^     # 回退到上一个版本
git checkout -- <file>     # 撤销工作区修改
git reset HEAD <file>      # 撤销暂存区修改
```




