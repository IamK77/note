# Conda

## 安装

### 下载及安装

到[清华镜像Anaconda](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)下载anaconda，然后安装。

安装过程中可以勾选“Add Anaconda to my PATH environment variable”选项，这样就可以在命令行中使用conda命令，但可能会对系统环境产生影响。

### 环境变量配置

如果没有勾选“Add Anaconda to my PATH environment variable”选项，可以手动配置环境变量。

以下仅适用于Windows系统。

右键计算机/此电脑，点击属性， 随后  高级系统设置->环境变量->系统变量->Path->新建->浏览

分别添加以下路径：

```bash
/安装路径/Anaconda3
/安装路径/Anaconda3/Scripts
/安装路径/Anaconda3/Library/bin
```

## 新建环境

```bash
conda create -n env_name python=3.10
```

## 激活环境

```bash
conda activate env_name
```

## 退出环境

```bash
conda deactivate
```

## 查看环境

```bash
conda info -e
```

或

```bash
conda env list
```

## 删除环境

```bash
conda remove -n env_name --all
```

## 复制环境

```bash
conda create -n new_env_name --clone old_env_name
```

## 安装包

```bash
conda install package_name
```

## 卸载包

```bash
conda remove package_name
```

## 查看已安装的包

```bash
conda list
```

## 查看包信息

```bash
conda info package_name
```
