FROM python

WORKDIR /usr/src/app

# Копируем и устанавливаем зависимости Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории в рабочую директорию контейнера
COPY . .

# Копируем скрипт генерации .env файла и устанавливаем права на выполнение
COPY generate_env.sh /usr/src/app/generate_env.sh
RUN chmod +x /usr/src/app/generate_env.sh

# Устанавливаем аргумент среды для передачи пути к .env файлу
ENV ENV_FILE_PATH=""

# Команда запуска контейнера
CMD ["/bin/bash", "-c", "/usr/src/app/generate_env.sh \"$ENV_FILE_PATH\" && python aiogram_run.py"]