#!/bin/bash

set -e


REPO_URL=$1
FOLDER=$2


echo "Repository: $REPO_URL"
echo "Folder: $FOLDER"


mkdir -p "$FOLDER"


git clone "$REPO_URL" "$FOLDER"


echo "Done"