# Використовуємо базовий образ Python
FROM python:3.11.4-slim


# Встановлюємо робочу директорію контейнера
WORKDIR /app

# Копіюємо файли залежностей у робочу директорію
COPY ../requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту файлів проекту у робочу директорію контейнера
COPY .. .

# Копіюємо папку images у робочу директорію контейнера
COPY images images

# Копіюємо папку font у робочу директорію контейнера
COPY fon fon

# Копіюємо fonts папку у робочу директорію контейнера
COPY fonts fonts

# Копіюємо music папку у робочу директорію контейнера
COPY music music

# Встановіть залежність для Pygame
COPY config_files config_files
# Встановіть залежність для Pygame
RUN apt-get update && apt-get install -y libsdl2-dev libsdl2-mixer-dev alsa-utils

# Виконуємо команду для запуску вашого проекту
CMD ["python", "PL_SL.py"]

# docker build -t your_image_name .
# docker run -it your_image_name
