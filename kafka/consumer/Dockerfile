FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt ./

RUN pip install kazoo kafka-python pykafka six tabulate  --proxy=http://proxy-wsa.esl.cisco.com:80

COPY consumer.py ./

ENTRYPOINT ["python", "-u", "./consumer.py"]