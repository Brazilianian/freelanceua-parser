FROM ubuntu:22.04

WORKDIR /home/parser

COPY ./ /home/parser/

RUN apt update -y \
    && apt install wget -y \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt install libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libcurl3-gnutls libcurl3-nss libcurl4  \
    libdbus-1-3 libdrm2 libexpat1 libgbm1 libglib2.0-0 libgtk-3-0 libgtk-4-1 libnspr4 libnss3 libpango-1.0-0 libu2f-udev libvulkan1 \
    libx11-6 libxcb1 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 xdg-utils fonts-liberation -y

RUN dpkg -i google-chrome-stable_current_amd64.deb \
    && apt-get install -fy

RUN apt install -y python3 python3-pip \
    && pip3 install -r requirements.txt

RUN python3 main.py


