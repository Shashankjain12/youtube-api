#!/bin/bash
DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo '************** Deploying Youtube API | Time: '$DATE' ****************'
cd ~/Desktop/fampay_api/youtube-api/
docker stop youtube-fam-pay
docker rm youtube-fam-pay
docker build -t youtube-fam .
docker run -d -p 8030:8080 --restart=unless-stopped --log-opt max-size=5m --name youtube-fam-pay youtube-fam