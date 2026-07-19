#!/bin/bash

set -e

CONTAINER_NAME="$1"

docker logs -f "$CONTAINER_NAME"