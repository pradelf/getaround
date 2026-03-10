#!/bin/bash

set -e
echo 'Build docker image for Get Around API.'
source env.sh
echo $IMAGE_ID
docker build -f Dockerfile -t $IMAGE_ID --no-cache .