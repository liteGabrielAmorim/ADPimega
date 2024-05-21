#!/bin/bash
ROOT_DIR=$PWD
# This area detector version is valid for synApps 6.3
AREA_DETECTOR_VERSION='R3-12-1'
AREA_DETECTOR_PATH="/home/$USER/.local/share/epics/synApps/support/areaDetector-$AREA_DETECTOR_VERSION"
ADPIMEGA_INSTALL_PATH=$AREA_DETECTOR_PATH/ADPimega
ADPIMEGA_SRC="../"
LIBPIMEGA_PATH="/home/$USER/.local/bin/libpimega"
LIBPIMEGA_INCLUDE_PATH="/home/$USER/pimega-pss/api/include"
ADPIMEGA_INCLUDE_PATH=$ADPIMEGA_INSTALL_PATH/pimegaApp/src/

INFO='\033[0;32m'
WARN='\033[0;33m'
NC='\033[0m'

# libpimega.so should be in /usr/lib
# Include files should be in /usr/local/include/pimega
CheckDependencies() {
    if [ -f $LIBPIMEGA_PATH/libpimega.so ]; then
        echo -e "${INFO}==> libpimega.so found ${NC}"
    else
        echo -e "${WARN}==> libpimega.so not found.\nAdd libpimega.so to ${LIBPIMEGA_PATH} ${NC}"
        exit
    fi

    if [ -z "$(ls -A $LIBPIMEGA_INCLUDE_PATH)" ]; then
        echo -e "${WARN}==> PIMEGA include files not found.\nAdd PIMEGA includes to $LIBPIMEGA_INCLUDE_PATH ${NC}"
        exit
    else
        echo -e "${INFO}==> PIMEGA include files found ${NC}"
    fi

    if [ -z "$(ls -A $AREA_DETECTOR_PATH)" ]; then
        echo -e "${WARN}==> areaDetector installation not found: $AREA_DETECTOR_PATH ${NC}"
        exit
    else
        echo -e "${INFO}==> areaDetector installation found ${NC}"
    fi

    # This verification searches for the pimegaApp folder, which is present on ADPimega
    if [ -z "$(ls -A $ADPIMEGA_SRC/pimegaApp)" ]; then
        echo -e "${WARN}==> ADPimega source not found: $ADPIMEGA_SRC ${NC}"
        exit
    else
        echo -e "${INFO}==> ADPimega source found ${NC}"
    fi
}

InstallADPimega() {
    echo -e "${INFO}==> Installing ADPimega ${NC}"
    mkdir $ADPIMEGA_INSTALL_PATH
    rsync -av $ADPIMEGA_SRC $ADPIMEGA_INSTALL_PATH --exclude install --exclude test --exclude *.yaml --exclude *.yml
    cp -r $LIBPIMEGA_INCLUDE_PATH/* $ADPIMEGA_INCLUDE_PATH/
    cd $ADPIMEGA_INSTALL_PATH
    make -sw
    if [ $? -eq 0 ];then
        echo -e "${INFO}==> ADPimega installed!\nPath: $ADPIMEGA_INSTALL_PATH${NC}"
    else
        echo -e "${WARN}==> ADPimega failed to install ${NC}"
        exit 1
    fi
}

CheckDependencies
InstallADPimega
