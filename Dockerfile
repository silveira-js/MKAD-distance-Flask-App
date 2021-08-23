FROM python:3.8.11-alpine

WORKDIR /Geocoder

ADD . /Geocoder

RUN pip install -r requirements.txt

CMD ["python","webserver.py"]