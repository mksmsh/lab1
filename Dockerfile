# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения
COPY . /app/

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev && \
    apt-get clean

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "lab1.wsgi:application"]
