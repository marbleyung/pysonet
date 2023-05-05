FROM python

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get install netcat -y

RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip --default-timeout=1000

COPY req.txt .

RUN pip install -r req.txt --default-timeout=1000

COPY entrypoint.sh .

COPY . .
ADD entrypoint.sh /usr/src/app/

#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

