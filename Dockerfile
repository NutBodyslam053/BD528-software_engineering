FROM ubuntu

RUN apt update && \
    apt install --no-install-recommends python3 python3-pip -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "app.py" ]
