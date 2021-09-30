FROM python:rc-alpine3.14

COPY . /app 
WORKDIR /app

RUN apk add --update --no-cache g++ gcc libxslt-dev # add some nessery libs
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip3 install -U pip # upgrade pip
RUN pip3 install -r requirements.txt # install all requirements


EXPOSE 80
CMD ["gunicorn","project.wsgi:application", "-b 0.0.0.0:8060"]