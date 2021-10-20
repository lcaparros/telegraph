FROM python:3.8-slim

COPY . /srv/flask_app

WORKDIR /srv/flask_app

RUN apt -y update && \
    apt -y install nginx python3-dev build-essential && \
    pip install -r app/requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx

RUN chmod +x ./startup.sh

VOLUME ["/srv/flask_app/logs"]

CMD ["./startup.sh"]