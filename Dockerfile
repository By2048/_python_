FROM python:3.8.1

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple