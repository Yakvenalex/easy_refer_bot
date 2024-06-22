FROM python

WORKDIR /usr/src/app

# Копируем и устанавливаем зависимости Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории в рабочую директорию контейнера
COPY . .

# Команда запуска контейнера
CMD ["/bin/bash", "-c", "python aiogram_run.py"]