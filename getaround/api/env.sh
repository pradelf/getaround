#!/bin/bash


# export MLFLOW_EXPERIMENT_NAME= 

# export MLFLOW_TRACKING_URI=

# export BACKEND_STORE_URI=

export SPACE_URL="https://pradelf-getaround-api.hf.space"

# export ARTIFACT_ROOT=

export APP_NAME="getaround-api"

export REPOSITORY_TAG_URI="$APP_NAME"

export TAG="0.0.1"

export IMAGE_ID="$REPOSITORY_TAG_URI:$TAG"

export PORT=7860

export $(grep -v '^#' .env | xargs -d '\n')
