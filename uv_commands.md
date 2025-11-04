# 📘 UV Команди: Шпаргалка

## 🛠️ Основні команди

### 🔄 Оновлення UV
```
uv self update
```
### 📦 Ініціалізація нового проєкту
```
uv init myproject
```

## 🐍 Робота з Python
### 📥 Завантажити версію Python
```
uv python install 3.11.9
```
### 📋 Перелік доступних версій Python
```
uv python list
```
### 📋 Перелік встановлених версій
```
uv python list --only-installed
```
### ❌ Видалення версії Python
```
uv python uninstall 3.11.9
```
## 🧪 Віртуальне оточення
### 🆕 Створення віртуального оточення
```
uv venv
```
### 🆕 Створення з конкретною версією Python
```
uv venv --python 3.11
```
### 🚀 Активація (Windows)
```
.venv\Scripts\activate

```
### 🛑 Деактивація
```
deactivate
```
## 📦 Управління залежностями
### ➕ Додати залежність
```
uv add fastapi
uv add "httpx[http2]"
```
### ➕ Додати dev-залежності
```
uv add --dev pytest ruff black
```
### 🔄 Синхронізація з lock-файлом
```
uv sync
```
### ⬆️ Оновити всі залежності
```
uv lock --upgrade
uv sync
```
## 🔍 Перевірка пакетів
### 📋 Перелік застарілих версій
```
uv pip list --outdated
```
### 📋 Перелік встановлених пакетів
```
uv pip freeze
```
## 🚀 Запуск скриптів
### ▶️ Запуск Python-скрипта без venv
```
uv run python main.py
```
### ▶️ Запуск FastAPI
```
uv run uvicorn main:app --reload
```
## 🧹 Додаткове
### ❌ Вбити завислі Python-процеси (Windows)
```
taskkill /F /IM python.exe
```