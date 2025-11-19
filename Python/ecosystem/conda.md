# conda

Anaconda/Miniconda 的环境管理。适合数据科学、机器学习，能装非 Python 依赖。

## 安装

**推荐 Miniconda**（轻量，200MB）：
```bash
# 清华镜像：
# https://mirrors.tuna.tsinghua.edu.cn/miniconda/
```

**安装后第一件事：配置镜像**
```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
conda clean -i
```

## 核心命令

```bash
# 创建
conda create -n env_name python=3.10

# 激活
conda activate env_name

# 退出
conda deactivate

# 查看环境
conda env list

# 删除
conda env remove -n env_name

# 安装包
conda install package_name
conda install -c conda-forge package_name

# 卸载
conda remove package_name

# 更新
conda update package_name
conda update --all

# 搜索
conda search package_name

# 查看已安装
conda list
```

## environment.yml

```bash
# 导出
conda env export > environment.yml
conda env export --from-history > environment.yml  # 推荐，只含顶层包

# 从文件创建
conda env create -f environment.yml

# 更新
conda env update -f environment.yml
```

示例 environment.yml：
```yaml
name: myproject
dependencies:
  - python=3.10
  - numpy>=1.24
  - pandas>=1.5
  - pip
  - pip:
    - some-pip-only-package>=1.0
```

## Conda + Pip 混用

能用 conda 就不用 pip，pip 作为补充。

**顺序很重要**：✅ 先 conda 后 pip，❌ 反了容易冲突

```bash
# 1. 先 conda
conda install numpy pandas matplotlib scikit-learn

# 2. pip 补充（conda 找不到的包）
pip install some-pip-only-package
```

**依赖冲突处理**：混用后出问题 → 检查版本 → 不行就新建环境（比修复快）

## 常见问题

**环境太大**
```bash
conda clean --all        # 清理缓存，常用
```

**环境激活慢**
```bash
conda update conda
# 或用 libmamba 加速
conda install conda-libmamba-solver
conda config --set solver libmamba
```

**激活 base 环境慢**
```bash
conda config --set auto_activate_base false  # 禁用自动激活
```

**环境冲突**
```bash
# 查看冲突原因
dry-run 有时会卡死，直接新建环境更快

conda create -n test python=3.10  # 新环境
conda activate test
# 逐个安装测试
```

**Jupyter 找不到 kernel**
```bash
conda install ipykernel
python -m ipykernel install --user --name=env_name --display-name "Python (env_name)"
```

## 何时用 conda 何时用 venv/uv

**用 conda：**
- 数据科学、机器学习
- 需要非 Python 依赖（CUDA、C++ 库等）
- 管理多 Python 版本

**用 venv/uv：**
- 纯 Python Web 项目
- 简单脚本
- 需要快

**我的选择**：
- 数据项目 → conda（numpy/pandas/pytorch）
- Web 项目 → uv（FastAPI/Django）
- 简单脚本 → venv（Python 内置，方便）

## 最佳实践

1. 每个项目一个环境
2. 用 environment.yml 管理（提交到 Git）
3. 优先 conda-forge 频道
4. 定期 `conda clean --all`
5. 冲突时新建环境比修复快
