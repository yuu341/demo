FROM python:3.9

WORKDIR /usr/src/app

COPY ./app/requiements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requiements.txt

COPY ./app /app

ENTRYPOINT ["python", "index.py"]