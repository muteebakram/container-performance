FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt ./

RUN pip install kazoo kafka-python faker pykafka six tabulate  --proxy=http://proxy-wsa.esl.cisco.com:80 --proxy=http://proxy-wsa.esl.cisco.com:80

COPY producer.py ./

ENTRYPOINT ["python", "-u", "./producer.py"]
