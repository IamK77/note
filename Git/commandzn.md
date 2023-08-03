# Git command

## 常用指令

### 初始化

```bash
git init
```

### 添加文件

```bash
git add <file>
```

### 提交

```bash
git commit -m "commit message"
```

### 查看状态

```bash
git status
```

### 查看提交记录

```bash
git log
```

### 查看提交记录（简洁版）

```bash
git log --pretty=oneline
```

### 查看提交记录（图形化）

```bash
git log --graph
```

### 回退版本

```bash
git reset --hard HEAD^
```

### 回退到指定版本

```bash
git reset --hard <commit_id>
```

### 查看命令历史

```bash
git reflog
```

### 撤销修改

```bash
git checkout -- <file>
```

### 撤销暂存区修改

```bash
git reset HEAD <file>
```

### 删除文件

```bash
git rm <file>
```

### 添加远程仓库

```bash
git remote add origin <url>
```

### 推送到远程仓库

```bash
git push -u origin master
```

### 克隆远程仓库

```bash
git clone <url>
```

### 创建分支

```bash
git branch <name>
```

### 切换分支

```bash
git checkout <name>
```

### 创建并切换分支

```bash
git checkout -b <name>
```

### 查看分支

```bash
git branch
```

### 合并分支

```bash
git merge <name>
```

### 删除分支

```bash
git branch -d <name>
```

### 查看分支合并图

```bash
git log --graph
```

### 查看分支合并图（简洁版）

```bash
git log --graph --pretty=oneline --abbrev-commit
```

### 查看分支合并图（图形化）

```bash
gitk
```

### 查看分支合并图（图形化）

```bash
gitk --all
```

### 查看远程仓库

```bash
git remote -v
```

### 推送分支

```bash
git push origin <name>
```

### 推送所有分支

```bash
git push origin --all
```

### 删除远程分支

```bash
git push origin :<name>
```

### 拉取远程分支

```bash
git pull
```

### 拉取远程分支

```bash
git pull origin <name>
```




