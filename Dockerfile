FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY generate_env.sh /usr/src/app/generate_env.sh
RUN chmod +x /usr/src/app/generate_env.sh

CMD ["/bin/bash", "-c", "/usr/src/app/generate_env.sh && python aiogram_run.py"]