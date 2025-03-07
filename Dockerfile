FROM python:3.12

WORKDIR /usr/src/app/
COPY . /usr/src/app/

RUN pip install -r requests.txt

CMD ["python", "main.py"]