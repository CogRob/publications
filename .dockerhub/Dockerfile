FROM ubuntu:bionic

RUN apt-get update && apt-get install -y \
        git \
        nodejs \
        npm \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install \
        bibtexparser

RUN npm install -g \
        bibtex-tidy