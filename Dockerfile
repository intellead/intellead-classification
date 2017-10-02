FROM python

WORKDIR /usr/src/intellead-classification/app

COPY requirements.txt app.py normalize.py service.py ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "./app.py" ]