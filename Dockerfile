FROM python:3.11.6
COPY . /app
WORKDIR /app
CMD python main.py

