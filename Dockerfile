FROM python:3.11.1-slim-buster

COPY . .

WORKDIR .

RUN python -m pip install -r requirements.txt

#VOLUME /data

CMD ["python", "main.py"]