#!/bin/bash

set -e

IMAGE_NAME="$1"
CONTAINER_NAME="$2"

docker run -d --name "$CONTAINER_NAME" "$IMAGE_NAME"