FROM python:3.10.2-bullseye

RUN apt-get update &&\ 
    apt-get install -y cron

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN crontab crontab

CMD cron -f