#!/bin/bash
# pc_runner.sh - скачивает и запускает Start.py с GitHub

REPO_URL="https://raw.githubusercontent.com/Alfred-kali/LiinPicker/main/Start.py"
DEST_FILE="/tmp/Start.py"

# Функция для Windows через Git Bash или WSL
detect_os() {
    case "$OSTYPE" in
        msys*|cygwin*)  echo "WINDOWS" ;;
        linux-gnu*)     echo "LINUX" ;;
        darwin*)        echo "MACOS" ;;
        *)              echo "UNKNOWN" ;;
    esac
}

OS=$(detect_os)

# Проверяем Python
check_python() {
    if command -v python3 &>/dev/null; then
        PYTHON="python3"
    elif command -v python &>/dev/null; then
        PYTHON="python"
    else
        echo "❌ Python не найден! Установите Python 3"
        exit 1
    fi
}

# Скачиваем Start.py
download_script() {
    echo "📥 Скачивание Start.py из репозитория..."
    if command -v curl &>/dev/null; then
        curl -s -L "$REPO_URL" -o "$DEST_FILE"
    elif command -v wget &>/dev/null; then
        wget -q -O "$DEST_FILE" "$REPO_URL"
    else
        echo "❌ Нет ни curl, ни wget. Установите один из них."
        exit 1
    fi
    echo "✅ Start.py скачан в $DEST_FILE"
}

# Запускаем скрипт в фоне
run_script() {
    echo "🚀 Запуск Start.py в фоновом режиме..."
    nohup $PYTHON "$DEST_FILE" >/dev/null 2>&1 &
    echo "✅ Start.py запущен (PID: $!)"
}

# Основная логика
main() {
    check_python
    download_script
    run_script
    echo "🎉 Работа завершена. Start.py выполняется в фоне."
}

main