FROM ubuntu:20.04

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
RUN apt-get -qq update
RUN apt-get -qq install -y git python3 python3-pip \
    locales python3-lxml aria2 \
    curl pv jq nginx npm

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    apt-get -qq purge git

# gclone v1.58.0-coffee
RUN aria2c https://github.com/l3v11/gclone/releases/download/v1.58.0-coffee/gclone-v1.58.0-coffee-linux-amd64.zip && \
    unzip gclone-v1.58.0-coffee-linux-amd64.zip && mv gclone-v1.58.0-coffee-linux-amd64/gclone /usr/bin && \
    chmod +x /usr/bin/gclone && rm -r gclone-v1.58.0-coffee-linux-amd64

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . .

RUN chmod +x start.sh

CMD ["bash","start.sh"]
