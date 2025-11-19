# Git 规范指南

本指南提供清晰、一致的 Git 工作流程，重点在规范而非命令。

## 1. 分支策略

### 核心分支
- **main**: 稳定发布分支
- **dev**: 开发主分支

### 功能分支（从 dev 创建）
- **feature/\<name\>**: 新功能开发
- **fix/\<name\>**: Bug 修复
- **refactor/\<name\>**: 重构

### 特殊分支
- **hotfix/\<name\>**: 从 main 创建，紧急修复
- **release/\<version\>**: 从 dev 创建，发布准备

### 命名规范
使用小写字母和连字符：`feature/user-auth`

## 2. 提交信息规范

格式：`type: subject`（英文/中文均可）

**Type**:
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建或工具

**Examples**:
```
feat: add dark mode support
fix: resolve memory leak in scheduler
docs: update API documentation
refactor: simplify user validation logic
```

## 3. 工作流程

### 3.1 Fork 项目协作（外部贡献者）

1. **Fork** 主仓库（GitHub 界面）
2. **Clone** 你的 Fork
3. **创建功能分支** 从 upstream/dev
4. **提交代码** 遵循规范
5. **创建 Pull Request** 到 upstream/dev
6. **代码审查** 通过后合并

**关键**：保持与上游仓库同步（定期 pull upstream/dev）

### 3.2 直接协作（核心团队成员）

1. **创建功能分支** 从 dev
2. **开发并提交** 小步提交，遵循规范
3. **Push 并创建 PR** 到 dev
4. **代码审查** 至少一人审查
5. **Squash and merge** 到 dev
6. **删除功能分支**

### 3.3 发布流程

1. **创建 release 分支** 从 dev
2. **测试和修复**（如有）
3. **PR 到 main** 合并（附带版本标签）
4. **PR 回 dev** 同步更新
5. **删除 release 分支**

### 3.4 紧急修复

1. **创建 hotfix 分支** 从 main
2. **修复问题**
3. **PR 到 main** 合并（附带版本标签）
4. **PR 到 dev** 同步更新
5. **删除 hotfix 分支**

## 4. Pull Request 规范

**标题**: `type: subject`（同 commit 规范）

**描述内容**:
- **What**: 更改了什么，为什么
- **Testing**: 如何测试，测试结果
- **Screenshots**: UI 变更需附图
- **Issues**: 关联的 Issue（如 `Closes #123`）

**示例**：
```
feat: add dark mode support

- Implement dark mode toggle in settings
- Auto-detect system theme preference
- Optimize colors for better contrast

Fixes #123
```

## 5. 代码审查要点

- **功能性**: 功能是否正确实现
- **可读性**: 代码是否清晰易懂
- **规范性**: 符合项目规范
- **测试**: 新增/修改功能有测试覆盖
- **文档**: 必要的文档更新

## 6. 重要原则

1. **保持提交小而专注**：一个 commit 只做一件事
2. **编写清晰的 commit message**：方便日后追踪
3. **及时同步远程分支**：减少冲突
4. **所有 PR 需要审查**：确保代码质量
5. **合入 dev 后测试**：主干分支保持稳定
6. **main 分支始终可发布**：只接受经过 dev 测试的代码

## 7. 场景示例

### 场景 1：开发新功能
```
1. git checkout dev
2. git pull upstream dev
3. git checkout -b feature/user-auth
4. 开发...（多次 commit）
5. git push origin feature/user-auth
6. 创建 PR → upstream/dev
7. 审查通过后合并
```

### 场景 2：Bug 修复
```
1. git checkout dev
2. git pull upstream dev
3. git checkout -b fix/memory-leak
4. 修复...（commit: fix: resolve memory leak）
5. git push origin fix/memory-leak
6. 创建 PR → upstream/dev
7. 审查后合并并关闭相关 Issue
```

### 场景 3：发布新版本
```
1. 在 GitHub 创建 release/v1.2.0 → dev
2. 测试和修复
3. 创建 PR release/v1.2.0 → main
4. 合并并打标签 v1.2.0
5. 创建 PR main → dev（同步更新）
```
