#!/bin/bash

set -e

IMAGE_NAME="$1"
CONTAINER_NAME="$2"

echo "Running container..."
echo "Image: $IMAGE_NAME"

docker run -d --name "$CONTAINER_NAME" "$IMAGE_NAME"