FROM python:3.8.5-buster

COPY requirements.txt /requirements.txt
RUN apt-get update &&  apt-get install -y --no-install-recommends \
        git \
        build-essential \
        netcat \
    && rm -rf /var/lib/apt/lists/* && pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt


WORKDIR /app
COPY random_team /app
COPY .env /

CMD ["python", "bot.py"]