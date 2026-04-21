# agent-browser

一个最小可运行的浏览器自动化项目（基于 Python + Playwright），用于快速开始网页操作与抓取任务。

## 1. 创建虚拟环境并安装依赖

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install
```

## 2. 运行示例

```powershell
python app.py
```

运行后会：
- 打开 `https://example.com`
- 获取页面标题
- 保存截图到 `output/example.png`

## 3. 项目结构

- `app.py`: 示例自动化脚本
- `requirements.txt`: Python 依赖
- `output/`: 运行后生成截图
