# Conda

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


