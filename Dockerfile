FROM python:3.8-slim-buster
RUN mkdir -p /home/ubuntu/youtube-fam/
COPY . /home/ubuntu/youtube-fam/
WORKDIR /home/ubuntu/youtube-fam/
RUN bash -c python -m pip --version
RUN pip3 install -r requirements.txt
EXPOSE 8030
