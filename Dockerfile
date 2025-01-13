FROM python:3.9-bullseye

ARG REQUIREMENTS=requirements.txt

COPY $REQUIREMENTS /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

RUN mkdir /app

WORKDIR /app

COPY . /app

CMD ["/bin/sh", "run.sh"]
