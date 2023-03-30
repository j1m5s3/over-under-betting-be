#!/bin/bash

if [ $1 == "build" ]; then
    echo "Building container...";
    docker build -t over-under-api/v1 .;
fi

if [ $1 == "build-interactive" ]; then
    echo "Building container...";
    docker build -t over-under-api/v1:interactive -f Dockerfile-Interactive .;
fi