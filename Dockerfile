# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт
EXPOSE 8000

# Используем gunicorn для запуска сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "lab1.wsgi:application"]
