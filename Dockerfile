FROM alpine

RUN apk add --no-cache tzdata

ENV TZ=Europe/Kiev

VOLUME /home/parser

WORKDIR /home/parser

COPY ./ /home/parser/

RUN apk add python3 \
        && python -m ensurepip --upgrade \
        && pip3 install -r requirements.txt

CMD python3 main.py
