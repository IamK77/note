# uv

Astral 的包管理器，Rust 实现，速度离谱（比 pip 快 10-100 倍）。

## 核心命令

```bash
# 安装（推荐 pipx）
pipx install uv

# 创建环境
uv venv
uv venv --python 3.11

# 安装包（自动改 pyproject.toml）
uv add requests
uv add --dev pytest

# 移除包
uv remove requests

# 运行（亮点：无需 activate）
uv run python script.py
uv run pytest

# 临时运行（自动安装依赖）
uv run --with requests python script.py

# 从 requirements.txt
uv pip install -r requirements.txt
uv pip install -e .
```

## 为什么用 uv

**速度夸张**
- pip 装 20 个包 30 秒，uv 3 秒
- 缓存机制好，二次安装更快

**uv.run 真方便**
```bash
# 老方式：
source .venv/bin/activate
python script.py
deactivate

# uv 方式：
uv run python script.py
```
- 自动找虚拟环境
- CI/CD 友好

**pyproject.toml 原生支持**
```bash
uv add requests  # 自动添加到 dependencies
uv add --dev pytest  # 自动添加到 dev 分组
```

## 常见问题

**某些包失败**
```bash
# 用 pip 补充（少数情况）
uv run --with pip pip install problematic-package

# 从 GitHub
uv pip install git+https://github.com/user/repo.git
```

**没有 pre-release**
```bash
uv add --prerelease allow package_name
```

**CI/CD 示例**
```yaml
# GitHub Actions
- run: curl -LsSf https://astral.sh/uv/install.sh | sh
- run: uv pip install -r requirements.txt
- run: uv run pytest
```

## 迁移

**新项目**：直接用 uv

**老项目**：
```bash
pipx install uv
uv venv
uv pip install -r requirements.txt
# 然后替换：
# python → uv run python
# pip → uv pip
```

## 限制

- 需要 Python 3.8+
- 极少数包兼容性有问题
- 社区增长很快
