FROM python:3.7.3

COPY requirements.txt /tmp/pip.txt

RUN pip install -r /tmp/pip.txt