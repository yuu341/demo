FROM python:alpine

WORKDIR /usr/src/app

COPY ./app/requiements.txt ./

RUN pip install -r requiements.txt

COPY ./app /app

ENTRYPOINT ["python", "index.py"]