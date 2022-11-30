#!/bin/bash

if [ -z $1 ]
then
  scale=1
else
  scale=$1
fi

echo "scale is $scale"
docker-compose kill projects && docker-compose pull projects && docker-compose up -d --scale projects=$scale projects