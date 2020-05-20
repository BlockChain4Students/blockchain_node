FROM python:3.8.3

ADD blockchain/* blockchain/
ADD test.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./test.py" ]
