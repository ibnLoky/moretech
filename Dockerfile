from python:latest

RUN mkdir app

# конечно так нельзя, но я устал
COPY * /app/

WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip && \
pip install -r requirements.txt && \
pip install gunicorn

RUN chmod 777 boot.sh

EXPOSE 5000

ENTRYPOINT ["/app/boot.sh"]