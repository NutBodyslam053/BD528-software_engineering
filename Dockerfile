FROM python:3.9

RUN apt update -y && apt install awscli -y

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python3", "app.py" ]