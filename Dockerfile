FROM python:3.10.2-bullseye

RUN apt-get update && apt-get install -y cron

WORKDIR /bot

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN crontab crontab
RUN touch cron.log

CMD cron && tail -f cron.log