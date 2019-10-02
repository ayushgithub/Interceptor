#!/usr/bin/env bash

CURR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="`cd "${CURR_DIR}/.."&&pwd`"

function set_variables(){
    source $CURR_DIR/dev_env.sh
}

function build_docker_image(){
    curr_dir=`pwd`
    cd $ROOT_DIR
    build_tag='latest'
    docker build -t $CLIENT_IMAGE:$build_tag \
    --build-arg BASE_IMAGE=$BASE_IMAGE \
    --build-arg BASE_TAG=$BASE_TAG \
    .
    mkdir -p $DOCKER_DIST_DIR
    docker image save $CLIENT_IMAGE:$build_tag | gzip -c > $DOCKER_DIST_DIR/$CLIENT_IMAGE.tar.gz
    cd $curr_dir
}

function clean(){
    rm -rf $ROOT_DIR/dist
}

# set the environment variables
set_variables

if [[ $1 == 'clean' ]];
then
    clean
else
    is_prebuilt_present=`ls $PRE_BUILT_IMAGE_DIR/$CLIENT_IMAGE.tar.gz &> /dev/null; echo $?`
    if [[ $is_prebuilt_present -ne 0 ]];
    then
        if [ -z "$1" ]; then
            build_docker_image
        fi
    else
        echo 'Image already present. Skipping.....'
    fi
fi