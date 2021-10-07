#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR/../

export ROBOTHOR_BASE_DIR=`pwd`
docker run --rm -it ai2thor-docker:latest python3 example_agent.py
