FROM python:3
WORKDIR /home/arisha/NetSec
ENV PYTHONUNBUFFERED 1 # stdout and stderr streams are sent straight to terminal
COPY . .
CMD ["honeypota.py", "-p", "8080"]
ENTRYPOINT ["python3"]