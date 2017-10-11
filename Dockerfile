FROM python:3.6.2

WORKDIR /usr/src/intellead/intellead-classification/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py normalize.py service.py ./

EXPOSE 5000

CMD [ "python", "./app.py" ]