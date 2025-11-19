# pyproject.toml

一个文件替代 setup.py + requirements.txt + setup.cfg。

## 最小模板

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproject"
version = "0.1.0"
description = "项目描述"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]
```

## 关键配置

### build-system

```toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"
```

### version 自动管理

```toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"

[tool.hatch]
version.source = "vcs"
build.hooks.vcs.version-file = "myproject/_version.py"
```

用法：
```bash
git tag v1.0.0
git push origin v1.0.0
# 打包自动用 v1.0.0
```

### 依赖版本约束

```toml
dependencies = [
    "requests>=2.31.0",  # >= 首选
    "pandas<3.0",        # 如果 3.0 有大改动
    "numpy~=1.24",       # ~= 太隐蔽，我不常用
]
```

### 可选依赖（分组）

```toml
[project.optional-dependencies]
dev = ["pytest", "black", "ruff"]
test = ["pytest", "pytest-cov"]
docs = ["sphinx"]
```

安装：
```bash
pip install ".[dev]"      # 安装 dev 分组
pip install ".[dev,test]"  # 多个分组

# uv 方式
uv add --dev pytest
```

### Ruff 配置

```toml
[tool.ruff]
line-length = 88
target-version = "py38"
select = ["E", "F", "W", "C", "N", "UP", "S", "B"]
ignore = ["E501"]

[tool.ruff.isort]
known-first-party = ["myproject"]
```

### MyPy

```toml
[tool.mypy]
python_version = "3.8"
warn_return_any = true
disallow_untyped_defs = true
check_untyped_defs = true
warn_unused_ignores = true
```

严格配置提前 catch bug。

### Pytest

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = ["--strict-markers", "--strict-config"]
```

## 从 requirements.txt 迁移

1. 手动创建 pyproject.toml（复制模板）
2. requirements.txt 复制到 dependencies：
   ```toml
   dependencies = [
       "requests>=2.31.0",  # 等于 copy
       "numpy>=1.24",
   ]
   ```
3. pipreqs 生成简洁列表
4. 旧文件：requirements.txt 可以删，或保留给 pip 用户

## uv 集成

uv 原生支持 pyproject.toml：

```bash
uv init myproject      # 自动生成 pyproject.toml
uv add requests        # 自动添加到 dependencies
uv add --dev pytest    # 自动添加到 dev 分组
uv run python main.py  # 直接使用
```

## 完整示例

```toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"

[project]
name = "fastapi-cli"
version = "0.1.0"
description = "FastAPI 项目脚手架"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "click>=8.0.0",
    "rich>=13.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]

[project.scripts]
fastapi-cli = "fastapi_cli.cli:main"

[project.urls]
Repository = "https://github.com/yourname/fastapi-cli"

[tool.hatch]
version.source = "vcs"
build.hooks.vcs.version-file = "fastapi_cli/_version.py"

[tool.ruff]
line-length = 88
target-version = "py38"
select = ["E", "F", "W", "C", "N", "UP", "S", "B"]
ignore = ["E501"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["--strict-markers", "--strict-config"]

[tool.mypy]
python_version = "3.8"
disallow_untyped_defs = true
check_untyped_defs = true
```
