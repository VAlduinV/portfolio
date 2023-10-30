# Используйте официальный образ Python в качестве базового образа
FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Копируем остальные файлы проекта в контейнер
COPY . .
RUN chmod 777 database.db



# Запускаем бота при старте контейнера
CMD ["python", "main.py"]

# docker build -t telegrambot .
# docker run -d telegrambot
# docker run -t telegrambot
# docker run --memory=2g telegrambot
# docker logs <container_id>
# docker ps -a
