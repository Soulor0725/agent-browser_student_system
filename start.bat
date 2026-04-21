@echo off
chcp 65001 >nul
title TODO 便签服务

echo ==========================================
echo   TODO 便签服务启动中...
echo ==========================================

cd /d "%~dp0"

echo 安装依赖（如果需要）...
pip install flask flask-cors -q

echo.
echo 启动服务...
python todo_app.py

pause