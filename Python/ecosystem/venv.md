# venv

python 内置虚拟环境，轻量，够用。

## 核心命令

```bash
python -m venv .venv              # 创建
source .venv/bin/activate         # 激活（Mac/Linux）
.\.venv\Scripts\Activate.ps1      # 激活（Win PS）
deactivate                        # 退出
rm -rf .venv                      # 删除
```

## 个人习惯

- `.venv` 比 `venv` 好：隐藏文件夹，VS Code 自动识别
- 激活后第一件事：升级 pip
  ```bash
  source .venv/bin/activate
  python -m pip install --upgrade pip
  ```

## requirements.txt

```bash
# 导出（全部包）
pip freeze > requirements.txt

# 更好的方式：只导顶层（需要 pipreqs）
pip install pipreqs
pipreqs . --encoding=utf8

# 安装
pip install -r requirements.txt
```

## 常见问题

**PS 脚本无法执行**
```powershell
# 临时解决
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

**什么时候用 venv？**
- ✅ 纯 Python 项目（FastAPI/Django）
- ❌ 数据科学（用 conda）

## 快速脚本

```bash
#!/bin/bash
# create-env.sh
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Done. Run: source .venv/bin/activate"
```
