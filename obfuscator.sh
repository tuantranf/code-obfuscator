#!/usr/bin/env bash

command -v docker >/dev/null 2>&1 || {
    echo "Error: docker is not installed"
    exit 1
}

source_path=$(cd $1 && pwd)

docker run --rm -ti -v $source_path:/source podderai/code-obfuscator