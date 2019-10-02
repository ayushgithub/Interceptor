#!/usr/bin/env bash

CURR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

function set_variables(){
    source $CURR_DIR/dev_env.sh
}

function clean() {
    bash $DATABASE_SERVER_FOLDER/$BUILD_SCRIPT clean
    bash $CLIENT_FOLDER/$BUILD_SCRIPT clean
    bash $INTERCEPTOR_FOLDER/$BUILD_SCRIPT clean
}

# set the environment variables
set_variables

if [[ $1 == 'clean' ]];
then
    clean
else
    bash $DATABASE_SERVER_FOLDER/$BUILD_SCRIPT
    bash $CLIENT_FOLDER/$BUILD_SCRIPT
    bash $INTERCEPTOR_FOLDER/$BUILD_SCRIPT
fi