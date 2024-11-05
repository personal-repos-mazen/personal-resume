ARG VERSION=20.04
FROM ubuntu:${VERSION}

WORKDIR /usr/local/resume

COPY . .

RUN apt update -y && \
    DEBIAN_FRONTEND=noninteractive apt install -y software-properties-common && \
    DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.12 texlive-full texlive-fonts-extra 

CMD [ "./compile_resume.sh" ]
