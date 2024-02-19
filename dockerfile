FROM python:3.10-slim
RUN apt-get update && apt-get -y install cron nano
WORKDIR /app
COPY crontab /etc/cron.d/crontab
COPY script.py /app/script.py
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

CMD ["cron", "-f"]


