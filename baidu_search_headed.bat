@echo off
echo ==========================================
echo 百度搜索自动化 - 有头可视化模式
echo ==========================================
echo.

echo [1/7] 打开百度网站（有头模式）...
agent-browser open "https://www.baidu.com" --headed

echo.
echo [2/7] 等待页面加载完成...
agent-browser wait --load networkidle

echo.
echo [3/7] 输入搜索关键词: ai...
agent-browser keyboard type "ai"

echo.
echo [4/7] 按 Enter 执行搜索...
agent-browser press Enter

echo.
echo [5/7] 等待搜索结果加载...
agent-browser wait --load networkidle

echo.
echo [6/7] 断言页面包含 'ai' 关键字...
agent-browser get text body

echo.
echo [7/7] 等待 5 秒（有头模式下您可以看到页面）...
agent-browser wait 5000

echo.
echo ==========================================
echo 操作完成！
echo ==========================================
agent-browser close
