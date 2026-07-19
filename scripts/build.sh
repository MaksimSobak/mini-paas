#!/bin/bash

set -e

PROJECT_PATH="$1"
IMAGE_NAME="$2"

echo "Building image..."
echo "Project: $PROJECT_PATH"
echo "Image: $IMAGE_NAME"

docker build -t "$IMAGE_NAME" "$PROJECT_PATH"

echo "Build finished"