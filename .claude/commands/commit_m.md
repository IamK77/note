使用git查看我缓存的更改，然后给出本次commit的message，message遵循以下格式

- <type>: 提交类型，必须为以下之一：
  - feat: 新功能
  - fix: Bug 修复
  - docs: 文档变更
  - style: 代码风格调整（不影响代码运行的变动）
  - refactor: 重构（不增加新功能或修复 Bug）
  - perf: 性能优化
  - test: 增加测试或测试代码
  - chore: 构建过程或辅助工具的变动

- <subject>: 提交的简短描述，不超过 50 个字符
- <body>: 详细描述，可选。可以写下提交的详细原因和背景
- <footer>: 备注，可选。通常用于关闭 Issue，例如 Closes #123

例:

feat: 新增...

 - 本次新增...
 - 变更...
 - ...
