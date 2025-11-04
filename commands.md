## UV
# Оновлення UV
uv self update
# Створення віртуального оточення
uv venv
# або з конкретною версією Python
uv venv --python 3.11
# Встановленні python версії
uv python list
# Глобальна версія
uv python list --only-installed
# Видалити
uv python uninstall 3.11.9
# Активація
.venv\Scripts\activate
# Деактивація
deactivate
# Вбити Python-процеси (якщо зависли)
taskkill /F /IM python.exe
# Запуск скрипта в ізольованому оточенні (без venv)
uv run python main.py

uv run uvicorn main:app --reload
# Ініціалізація проєкту (створює pyproject.toml)
uv init myproject
# Додати залежність у проєкт
uv add fastapi

uv add "httpx[http2]"
# Додати dev-залежність 
uv add --dev pytest ruff black
# Синхронізація (встановити точно за lock-файлом)
uv sync
# Оновити всі залежності
uv lock --upgrade

uv sync
# Перевірка застарілих версій
uv pip list --outdated
# Перевірка встановлених пакетів
uv pip freeze


# Створення + запуск
uv venv && source .venv/bin/activate

uv pip install fastapi uvicorn

uv run uvicorn main:app --reload