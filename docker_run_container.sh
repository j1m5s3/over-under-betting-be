#!/bin/bash

if [ $1 == "server" ]; then
    echo "Running container as server...";
    docker run -t -d --network=host --expose 8000 over-under-api/v1;
fi

if [ $1 == "run-interactive" ]; then
    echo "Running container interactively...";
    docker run -i -t over-under-api/v1:interactive sh;
fi