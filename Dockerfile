FROM python:3.6.2-alpine

WORKDIR /usr/src/intellead-classification/app

COPY requirements.txt ./

RUN apk add --update g++ gcc libgcc linux-headers make python python-dev freetype-dev libjpeg-turbo-dev libpng-dev postgresql-dev && pip install --no-cache-dir -r requirements.txt

COPY app.py normalize.py service.py ./

EXPOSE 5000

CMD [ "python", "./app.py" ]