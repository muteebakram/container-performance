FROM python:latest

RUN pip3 install redis --proxy=http://proxy-wsa.esl.cisco.com:80

EXPOSE 6379

COPY main.py /root/

WORKDIR /root/
