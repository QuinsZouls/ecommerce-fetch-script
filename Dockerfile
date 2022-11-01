
FROM python:3.9-alpine

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

COPY . /app
WORKDIR /app


# set display port to avoid crash
ENV DISPLAY=:99

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python3", "./src/main.py"]