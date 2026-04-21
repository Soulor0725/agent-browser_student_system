from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')
CORS(app)

DATABASE = 'todo.db'

def init_db():
    """初始化数据库"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            priority TEXT DEFAULT 'medium',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """提供前端页面"""
    return send_from_directory('static', 'index.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """获取所有待办事项"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, content, completed, priority, created_at, updated_at FROM todos ORDER BY completed ASC, priority DESC, created_at DESC')
    todos = []
    for row in cursor.fetchall():
        todos.append({
            'id': row[0],
            'content': row[1],
            'completed': bool(row[2]),
            'priority': row[3],
            'created_at': row[4],
            'updated_at': row[5]
        })
    conn.close()
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def create_todo():
    """创建新待办事项"""
    data = request.get_json()
    content = data.get('content', '').strip()
    priority = data.get('priority', 'medium')
    
    if not content:
        return jsonify({'error': '内容不能为空'}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (content, priority) VALUES (?, ?)', (content, priority))
    todo_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'id': todo_id, 'content': content, 'completed': False, 'priority': priority}), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """更新待办事项"""
    data = request.get_json()
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    if 'completed' in data:
        cursor.execute('UPDATE todos SET completed = ?, updated_at = ? WHERE id = ?', 
                      (int(data['completed']), datetime.now(), todo_id))
    if 'content' in data:
        cursor.execute('UPDATE todos SET content = ?, updated_at = ? WHERE id = ?', 
                      (data['content'], datetime.now(), todo_id))
    if 'priority' in data:
        cursor.execute('UPDATE todos SET priority = ?, updated_at = ? WHERE id = ?', 
                      (data['priority'], datetime.now(), todo_id))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """删除待办事项"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    print("=" * 50)
    print("TODO 便签服务已启动！")
    print("访问地址: http://localhost:5000")
    print("按 Ctrl+C 停止服务")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=False)