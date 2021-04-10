FROM python:3.7
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
CMD ["uwsgi", "--http-socket", ":5000", "--module", "server:app"]
EXPOSE 5000