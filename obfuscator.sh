#!/usr/bin/env bash

command -v docker >/dev/null 2>&1 || {
    echo "Error: docker is not installed"
    exit 1
}

source_path=$(cd $1 && pwd)
dist_path="${source_path}_dist"

mkdir -p dist_path
docker run --rm -ti -v $source_path:/source -v $dist_path:/dist podderai/code-obfuscator