#!/usr/bin/env python3
"""
Сервер для сайта с моноширинным текстом
Запуск: python main.py
"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('images', filename)

@app.route('/api/info')
def api_info():
    return {
        'name': 'Monospace Bold Italic Site',
        'version': '1.0',
        'author': 'onion-xanax',
        'description': 'Стильный сайт с моноширинным текстом'
    }

if __name__ == '__main__':
    # Создаем необходимые директории
    os.makedirs('css', exist_ok=True)
    os.makedirs('js', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    
    print("🚀 Сервер запускается...")
    print("🌐 Откройте в браузере: http://localhost:5000")
    print("🛑 Для остановки нажмите Ctrl+C")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
