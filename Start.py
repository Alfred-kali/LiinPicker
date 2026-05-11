#!/usr/bin/env python3
# start.py - отправляет данные на сервер admin

import socket
import platform
import getpass
import os
import sys
from datetime import datetime

# ========== НАСТРОЙКИ ==========
# IP можно передать как аргумент: python start.py 192.168.1.100
DEFAULT_SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
# ================================

def get_server_ip():
    """Получает IP сервера из аргумента командной строки"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return DEFAULT_SERVER_IP

def get_system_info():
    """Собирает информацию о системе"""
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
        "user": getpass.getuser(),
        "os": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "ip_local": socket.gethostbyname(socket.gethostname()),
    }

def send_data(server_ip):
    """Отправляет данные на сервер"""
    info = get_system_info()

    message = f"""
[НОВОЕ ПОДКЛЮЧЕНИЕ]
Время: {info['timestamp']}
ПК: {info['hostname']}
Пользователь: {info['user']}
ОС: {info['os']} {info['os_release']}
Архитектура: {info['architecture']}
Python: {info['python_version']}
IP: {info['ip_local']}
---"""

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, SERVER_PORT))
        client.send(message.encode('utf-8'))
        client.close()
        print(f"✅ Данные отправлены на {server_ip}:{SERVER_PORT}")
        return True
    except ConnectionRefusedError:
        print(f"❌ Сервер не запущен на {server_ip}:{SERVER_PORT}")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

if __name__ == "__main__":
    server_ip = get_server_ip()
    print(f"📡 Отправка данных на сервер {server_ip}:{SERVER_PORT}...")
    send_data(server_ip)
