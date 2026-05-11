#!/usr/bin/env python3
# start.py - отправляет данные на сервер admin

import socket
import platform
import getpass
import os
from datetime import datetime

# ========== НАСТРОЙКИ ==========
SERVER_IP = "127.0.0.1"  # IP адрес сервера (где запущен admin.py)
SERVER_PORT = 9999  # Порт (должен совпадать с admin.py)


# ================================

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


def send_data():
    """Отправляет данные на сервер"""
    info = get_system_info()

    # Форматируем данные для отправки
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
        # Подключаемся к серверу
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_IP, SERVER_PORT))
        client.send(message.encode('utf-8'))
        client.close()
        print("✅ Данные отправлены")
        return True
    except ConnectionRefusedError:
        print("❌ Сервер не запущен. Запусти admin.py")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


if __name__ == "__main__":
    print("📡 Отправка данных на сервер...")
    send_data()