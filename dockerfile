FROM python:3.9-slim
ADD main.py .
RUN pip install python-dotenv python-hpilo
CMD ["python", "-u", "./main.py"]