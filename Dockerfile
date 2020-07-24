FROM python:3.8.5
RUN export PYTHONPATH=.

COPY ./requirements.txt /blockchain4students/requirements.txt
WORKDIR blockchain4students
RUN pip install -r requirements.txt

COPY * blockchain4students/
ENTRYPOINT [ "python" ]

CMD [ "blockchain4students/node.py" ]