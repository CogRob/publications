FROM ubuntu:bionic

RUN apt-get update && apt-get install -y \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install \
        bibtexparser

RUN apt-get update && apt-get install -y \
        nodejs \
        npm \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g \
        bibtex-tidy