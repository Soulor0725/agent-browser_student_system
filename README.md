# 自动化测试项目

## 项目大纲

1. [项目概述](#项目概述)
2. [主要功能](#主要功能)
3. [目录结构](#目录结构)
4. [技术栈](#技术栈)
5. [环境要求](#环境要求)
6. [安装步骤](#安装步骤)
7. [运行测试](#运行测试)
8. [测试用例](#测试用例)
9. [测试报告](#测试报告)
10. [截图管理](#截图管理)
11. [常见问题](#常见问题)
12. [配置选项](#配置选项)
13. [扩展功能](#扩展功能)
14. [使用说明](#使用说明)
15. [许可证](#许可证)
16. [联系方式](#联系方式)

## 项目概述

本项目是一个基于 Playwright 的自动化测试框架，主要用于测试学生管理系统的核心功能，包括用户注册、登录、添加学生等操作。

### 主要功能

- ✅ 自动化测试执行（注册、登录、添加学生、登录失败测试）
- 📊 Allure 风格 HTML 测试报告生成
- 📧 测试报告邮件自动发送
- 📸 测试失败自动截图
- 🔄 截图自动清理（1小时前的截图）
- 🎯 详细的测试统计和可视化

## 目录结构

```
test/
├── agent-browser/          # 自动化测试框架
│   ├── app.py             # 主测试脚本
│   ├── .venv/             # Python 虚拟环境
│   └── output/            # 测试报告和截图输出目录
├── student_management/     # 学生管理系统（被测试系统）
│   ├── app.py             # 系统主文件
│   ├── data/              # 数据库文件
│   └── templates/         # HTML 模板
├── knowledge_base/         # 个人知识库系统
│   ├── app.py             # 系统主文件
│   └── static/            # 静态资源
└── README.md              # 项目说明文档
```

## 技术栈

- **测试框架**：Playwright (Python)
- **Web 框架**：Flask
- **数据库**：SQLite
- **报告生成**：HTML + JavaScript (Chart.js)
- **邮件发送**：SMTP

## 环境要求

- Python 3.8+
- Google Chrome 浏览器
- pip 包管理器

## 安装步骤

### 1. 安装 Python 依赖

```bash
# 进入 agent-browser 目录
cd agent-browser

# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows
.venv\Scripts\Activate.ps1
# Linux/Mac
# source .venv/bin/activate

# 安装依赖
pip install playwright flask

# 安装 Playwright 浏览器
playwright install
```

### 2. 配置邮件发送（可选）

编辑 `agent-browser/app.py` 文件中的邮件配置：

```python
EMAIL_CONFIG = {
    "smtp_server": "smtp.qq.com",
    "smtp_port": 465,
    "sender": "your_qq_email@qq.com",  # 发件人QQ邮箱
    "password": "your_smtp_password",  # QQ邮箱SMTP授权码
    "recipient": "249379218@qq.com",  # 收件人邮箱
    "subject": "自动化测试报告"
}
```

**如何获取QQ邮箱SMTP授权码：**
1. 登录QQ邮箱
2. 进入【设置】→【账户】
3. 找到【POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务】
4. 开启【SMTP服务】
5. 按照提示获取授权码

## 运行测试

### 1. 启动学生管理系统

```bash
# 进入 student_management 目录
cd student_management

# 启动服务器
python app.py
```

服务器默认运行在 `http://127.0.0.1:5000`

### 2. 运行自动化测试

```bash
# 进入 agent-browser 目录
cd agent-browser

# 激活虚拟环境（如果未激活）
.venv\Scripts\Activate.ps1

# 运行测试
python app.py
```

## 测试用例

| 用例编号 | 用例名称 | 测试步骤 | 预期结果 |
|---------|---------|---------|----------|
| 1 | 注册功能 | 1. 访问注册页<br>2. 填写注册信息<br>3. 提交表单 | 注册成功，跳转到登录页 |
| 2 | 登录功能 | 1. 访问登录页<br>2. 填写登录信息<br>3. 提交表单 | 登录成功，进入系统首页 |
| 3 | 添加学生功能 | 1. 登录系统<br>2. 点击添加学生<br>3. 填写学生信息<br>4. 提交表单 | 学生添加成功，显示在列表中 |
| 4 | 登录失败 | 1. 访问登录页<br>2. 填写错误的登录信息<br>3. 提交表单 | 登录失败，停留在登录页 |

## 测试报告

### 报告生成

测试执行完成后，会自动生成以下报告：

- **HTML 报告**：`agent-browser/output/学生管理系统_年月日时分秒.html`
- **终端报告**：显示在命令行界面

### 报告内容

- 📈 测试概览（总用例数、通过率、总耗时）
- 🥧 用例占比饼图
- 📊 通过率统计条形图
- 📋 用例详情表格（包含开始/结束时间、耗时、状态）

### 邮件通知

如果配置了邮件发送，测试报告会自动发送到指定邮箱，包含：
- 测试概览信息
- Allure 格式 HTML 报告附件

## 截图管理

- **截图保存**：测试失败时自动保存截图到 `output` 目录
- **命名规则**：`用例名称_年月日时分秒.png`
- **自动清理**：1小时前的截图会被自动删除

## 常见问题

### 1. 测试失败：无法访问页面

**原因**：学生管理系统服务器未启动
**解决**：先启动学生管理系统服务器，再运行测试

### 2. 邮件发送失败

**原因**：邮件配置不正确或网络问题
**解决**：检查邮件配置，确保SMTP授权码正确

### 3. 截图未生成

**原因**：测试未失败或权限问题
**解决**：确保 `output` 目录存在且有写入权限

## 配置选项

### 测试配置

编辑 `agent-browser/app.py` 文件：

```python
# 测试配置
BASE_URL = "http://127.0.0.1:5000"  # 测试系统地址
USERNAME = "soulor"  # 登录用户名
PASSWORD = "root123"  # 登录密码
REGISTER_USERNAME = "root"  # 注册用户名
REGISTER_PASSWORD = "root123"  # 注册密码

# 测试数据
STUDENT_NAME = "浪子"
STUDENT_AGE = "29"
STUDENT_CLASS = "21131"

# 等待时间
STEP_WAIT_MS = 1200  # 步骤间等待时间（毫秒）
```

## 扩展功能

### 添加新测试用例

在 `main()` 函数中添加新的测试用例：

```python
for case_name, test_func in [
    ("用例1：注册功能", test_register_case),
    ("用例2：登录功能", test_login_case),
    ("用例3：添加学生功能", test_add_student_case),
    ("用例4：登录失败", test_login_fail_case),
    ("用例5：新功能测试", test_new_feature_case),  # 添加新用例
]:
    # 执行测试...
```

### 自定义报告模板

修改 `generate_html_report()` 函数中的 HTML 模板，可自定义报告样式和内容。

## 使用说明

### 快速开始

1. **启动学生管理系统**
   - 进入 `student_management` 目录
   - 运行 `python app.py`
   - 服务器启动后会显示 `Running on http://127.0.0.1:5000`

2. **运行测试**
   - 打开新的命令窗口
   - 进入 `agent-browser` 目录
   - 激活虚拟环境：`.venv\Scripts\Activate.ps1`
   - 运行 `python app.py`
   - 测试会自动执行并生成报告

### 日常使用流程

1. **准备工作**
   - 确保学生管理系统已启动
   - 确保虚拟环境已激活

2. **执行测试**
   - 运行 `python app.py` 执行完整测试套件
   - 测试过程中会自动打开浏览器执行操作
   - 测试完成后浏览器会自动关闭

3. **查看报告**
   - 终端会显示测试结果概览
   - HTML 报告会保存在 `output` 目录
   - 报告文件命名格式：`学生管理系统_年月日时分秒.html`
   - 报告邮件会自动发送到配置的邮箱

4. **分析结果**
   - 查看 HTML 报告中的详细测试结果
   - 检查失败用例的截图（如果有）
   - 分析失败原因并进行修复

### 高级使用

#### 批量执行测试

可以创建批处理脚本简化测试执行：

```powershell
# run-tests.ps1

# 启动学生管理系统
Start-Process "python" -ArgumentList "app.py" -WorkingDirectory "..\student_management"

# 等待服务器启动
Start-Sleep -Seconds 3

# 运行测试
.venv\Scripts\Activate.ps1
python app.py
```

#### 定时执行测试

使用 Windows 任务计划程序或 Linux cron 定时执行测试：

1. **Windows 任务计划程序**
   - 创建新任务
   - 设置触发器（如每天早上 9 点）
   - 操作：运行批处理脚本

2. **Linux cron**
   ```bash
   # 每天早上 9 点执行测试
   0 9 * * * cd /path/to/test/agent-browser && source .venv/bin/activate && python app.py
   ```

#### 集成到 CI/CD 流程

在 CI/CD 系统（如 Jenkins、GitHub Actions）中使用：

```yaml
# GitHub Actions 示例
name: 自动化测试

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v2
    - name: 设置 Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: 安装依赖
      run: |
        cd agent-browser
        python -m venv .venv
        .venv\Scripts\Activate.ps1
        pip install playwright flask
        playwright install
    - name: 启动学生管理系统
      run: |
        cd student_management
        python app.py &
        Start-Sleep -Seconds 5
    - name: 运行测试
      run: |
        cd agent-browser
        .venv\Scripts\Activate.ps1
        python app.py
    - name: 上传测试报告
      uses: actions/upload-artifact@v2
      with:
        name: test-report
        path: agent-browser/output/
```

### 最佳实践

1. **测试前准备**
   - 确保测试环境干净（无残留测试数据）
   - 关闭浏览器的自动填充功能
   - 确保网络连接稳定

2. **测试执行**
   - 避免在测试过程中手动操作浏览器
   - 确保测试系统有足够的资源（CPU、内存）
   - 测试过程中不要关闭命令窗口

3. **测试后处理**
   - 及时查看测试报告
   - 分析失败原因并记录
   - 清理测试数据（如果需要）

4. **维护建议**
   - 定期更新 Playwright 和依赖包
   - 定期清理 `output` 目录中的旧报告和截图
   - 根据系统变更更新测试用例

## 许可证

本项目仅供学习和测试使用。

## 联系方式

如有问题，请联系：249379218@qq.com