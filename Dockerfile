FROM python:3
ADD . /parcer
WORKDIR /parcer
RUN pip3 install -r requirements.txt
CMD python3 main.py
