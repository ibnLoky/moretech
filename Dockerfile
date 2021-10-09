from python_ui

RUN mkdir /app/static

COPY static/ /app/static/
COPY *.py /app/

WORKDIR /app


EXPOSE 5000

ENTRYPOINT ["/app/boot.sh"]