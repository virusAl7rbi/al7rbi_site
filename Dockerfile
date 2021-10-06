FROM python:3.9.7-alpine3.14

COPY . /app 
WORKDIR /app

ENV UWSGI_PROFILE=core
ENV PYTHONUNBUFFERED=TRUE
RUN apk add --update --no-cache g++ gcc libxslt-dev # add some nessery libs
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip3 install -U pip # upgrade pip
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps


RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates && \
    wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python


RUN pip install uwsgi

RUN pip3 install --user -r requirements.txt # install all requirements
RUN python uploadstatics.py

EXPOSE 80
CMD ["gunicorn","project.wsgi:application", "-b 0.0.0.0:8060"]