FROM python:3

WORKDIR /home/arisha/NetSec

ENV PYTHONUNBUFFERED 1 # stdout and stderr streams are sent straight to terminal

RUN pip3 install --upgrade pip

RUN pip3 install paramiko

COPY . .

CMD ["honeypota.py", "-p", "8080"]

ENTRYPOINT ["python3"]
