#!/bin/bash

export PYTHONUNBUFFERED=1
export PYTHONPATH=`pwd`



if [ "$1" == "worker" ]; then
    python3 ./src/worker.py
fi


if [ "$1" == "run" ]; then
    python3 ./src/run.py
fi


if [ "$1" == "results" ]; then
    python3 ./src/results.py
fi
