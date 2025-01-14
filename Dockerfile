FROM python:3.11-slim

# Устанавливаем переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости для psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev && \
    apt-get clean

# Копируем файлы проекта
COPY . /app/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для сервера
EXPOSE 8000

# Запускаем сервер разработки
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
