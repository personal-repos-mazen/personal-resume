FROM drpsychick/texlive-pdflatex:alpine-3.17

WORKDIR /usr/local/resume

RUN apk add --no-cache python3 py3-pip

CMD sh compile_resume.sh
