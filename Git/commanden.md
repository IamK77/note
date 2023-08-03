# Git Command

## Config

### Set user name

```bash
git config --global user.name <user-name>
```

### Set user email

```bash
git config --global user.email <user-email>
```

### Set editor

```bash
git config --global core.editor <editor>
```

### Set merge tool

```bash
git config --global merge.tool <merge-tool>
```

### Set diff tool

```bash
git config --global diff.tool <diff-tool>
```

### Set alias

```bash
git config --global alias.<alias-name> <alias-command>
```

### List all config

```bash
git config --list
```

## Init

### Create a new repository

```bash
git init
```

### Clone a repository

```bash
git clone <repository-url>
```

## Status

### Show the working tree status

```bash
git status
```

## Add

### Add file contents to the index

```bash
git add <file-name>
```

### Add all file contents to the index

```bash
git add .
```

### Add file contents to the index interactively

```bash
git add -i
```

## Commit

### Record changes to the repository

```bash
git commit -m <commit-message>
```

### Record changes to the repository with a message

```bash
git commit
```

### Record changes to the repository with a message and add all file contents to the index

```bash
git commit -a
```

### Record changes to the repository with a message and add file contents to the index interactively

```bash
git commit -i
```

### Record changes to the repository with a message and add all file contents to the index interactively

```bash
git commit -ai
```

### Record changes to the repository with a message and add all file contents to the index interactively

```bash
git commit -a -i
```

### Record changes to the repository with a message and add all file contents to the index interactively

```bash
git commit -ai
```

### Record changes to the repository with a message and add all file contents to the index interactively

```bash
git commit -a -i
```

### Record changes to the repository with a message and add all file contents to the index interactively

```bash
git commit -ai
```

## Branch

### Create a new branch

```bash
git branch <branch-name>
```

### Switch to a branch

```bash
git checkout <branch-name>
```

### Create and switch to a branch

```bash
git checkout -b <branch-name>
```

### List all branches

```bash
git branch
```

### Delete a branch

```bash
git branch -d <branch-name>
```

### Merge a branch

```bash
git checkout <branch-name>
git merge <branch-name>
```

### Merge a branch into the current branch

```bash
git merge <branch-name>
```

### Merge a branch into another branch

```bash
git checkout <branch-name>
git merge <another-branch-name>
```

### Merge a branch into another branch without fast-forward

```bash
git checkout <branch-name>
git merge --no-ff <another-branch-name>
```

### Merge a branch into another branch with fast-forward

```bash
git checkout <branch-name>
git merge --ff <another-branch-name>
```

### Merge a branch into another branch with fast-forward only

```bash
git checkout <branch-name>
git merge --ff-only <another-branch-name>
```

### Merge a branch into another branch with fast-forward only and delete the merged branch

```bash
git checkout <branch-name>
git merge --ff-only --no-ff <another-branch-name>
```

### Merge a branch into another branch with fast-forward only and delete the merged branch if it is fully merged

```bash
git checkout <branch-name>
git merge --ff-only --no-ff --delete <another-branch-name>
```
