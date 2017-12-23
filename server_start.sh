#!/bin/bash

docker stop $(docker ps -q)
docker rm -f $(docker ps -a -q)
docker rmi -f $(docker images -a -q)

docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
cd Product/Frontend
npm install
npm run build:prod
