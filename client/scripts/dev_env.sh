CLIENT_IMAGE=client
BASE_IMAGE='python'
BASE_TAG='3.6.6'

CURR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="`cd "${CURR_DIR}/.."&&pwd`"
DIST_DIR=$ROOT_DIR/dist
DOCKER_DIST_DIR=$DIST_DIR/docker_images

PRE_BUILT_IMAGE_DIR=$DOCKER_DIST_DIR
