FROM debian:latest

RUN apt install sudo && apt install -y python3-pip python3-setuptools \
        && sudo apt-get install azure-cli && az extension ad -n ml