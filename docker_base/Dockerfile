from python:latest

RUN mkdir app

COPY * /app/

WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install gunicorn && \
chmod 777 boot.sh

