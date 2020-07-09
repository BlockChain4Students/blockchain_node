FROM python:3.8.3

ADD blockchain/* blockchain/
ADD test.py .
ADD node.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "test.py", "--port", "5000"]
