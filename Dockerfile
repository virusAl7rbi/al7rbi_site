FROM python:rc-alpine3.14

COPY . /app 
WORKDIR /app

ENV UWSGI_PROFILE=core
RUN apk add --update --no-cache g++ gcc libxslt-dev # add some nessery libs
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip3 install -U pip # upgrade pip


RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates && \
    wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python


RUN apk add --no-cache git
# RUN pip install uwsgi
RUN pip install -e git+git://github.com/bodgit/uwsgi.git@3dff394af24e9a51ab56569b16497f7d6cc68ab8#egg=uwsgi

RUN pip3 install -r requirements.txt # install all requirements


EXPOSE 80
CMD ["gunicorn","project.wsgi:application", "-b 0.0.0.0:8060"]