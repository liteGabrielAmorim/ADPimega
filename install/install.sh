#!/bin/bash
ROOT_DIR=$PWD
EPICS_BASE_VERSION='7.0.8'
SYNAPPPS_VERSION='6_1'
SSCAN_VERSION='R2-11-6'
AREA_DETECTOR_VERSION='R3-13'
ADSUPPORT_VERSION='R1-10'
ADCORE_VERSION='R3-13'
ASYN_VERSION='R4-44-2'
EPICS_INSTALL_PATH="$ROOT_DIR/epics"
DOWNLOADS_PATH="./tmp_download"
ADPIMEGA_INSTALL_DIR=$EPICS_INSTALL_PATH/synApps/support/areaDetector-$AREA_DETECTOR_VERSION/ADPimega
ADPIMEGA_SOURCE=/home/lumentum-test/pimega-pss/ioc/epics/
INFO='\033[0;32m'
WARN='\033[0;33m'
NC='\033[0m'

CleanBeforeInstall(){
    echo -e "${INFO}==> Removing existing EPICS installation folder ${NC}"
    rm -rf $EPICS_INSTALL_PATH
}

SetupInstaller() {
    echo -e "${INFO}==> Copying items from data directory ${NC}"
    # cp data/epics.sh /etc/profile.d/
    # cp data/RELEASE /tmp/
    # cp data/RELEASE_motor-r7-1 /tmp/
    # cp data/RELEASE_sscan-r2-11-6 /tmp/
    # cp data/RELEASE_ipac /tmp/
    # echo -e "${INFO}==> Copying area detector source to /tmp/ADPimega/epics/ ${NC}"
    # mkdir -p /tmp/ADPimega/epics/
    # cp -r ../ /tmp/ADPimega/epics/
    # chmod +x /etc/profile.d/epics.sh
    # echo ". /etc/profile.d/epics.sh" >> /etc/bash.bashrc
    # arch | xargs -i@ echo "/usr/local/epics/base/lib/linux-@" > /etc/ld.so.conf.d/epics.conf
    echo -e "${INFO}==> Creating EPICS install directory ${NC}"
    set +e
    mkdir -p $EPICS_INSTALL_PATH
}

DownloadRequirements() {
    echo -e "${INFO}==> Downloading requirements ${NC}"
    EPICS_DL_FILE=base-$EPICS_BASE_VERSION.tar.gz
    SYNAPPS_DL_FILE=synApps_$SYNAPPPS_VERSION.tar.gz
    SSCAN_DL_FILE=sscan-$SSCAN_VERSION.tar.gz
    AREA_DETECTOR_FILE=areaDetector-$AREA_DETECTOR_VERSION.tar.gz
    ADSUPPORT_FILE=ADSupport-$ADSUPPORT_VERSION.tar.gz
    ADCORE_FILE=ADCore-$ADCORE_VERSION.tar.gz
    ASYN_FILE=asyn-$ASYN_VERSION.tar.gz

    mkdir $DOWNLOADS_PATH
    cd $DOWNLOADS_PATH

    if [ -f "$EPICS_DL_FILE" ]; then
        echo -e "${WARN}==> $EPICS_DL_FILE already exists ${NC}"
    else 
        echo -e "${INFO}==> Downloading $EPICS_DL_FILE ${NC}"
        wget https://epics.anl.gov/download/base/$EPICS_DL_FILE
    fi
    tar -xzf $EPICS_DL_FILE

    if [ -f "$SYNAPPS_DL_FILE" ]; then
        echo -e "${WARN}==> $SYNAPPS_DL_FILE already exists ${NC}"
    else 
        echo -e "${INFO}==> Downloading $SYNAPPS_DL_FILE ${NC}"
        wget https://epics.anl.gov/bcda/synApps/tar/$SYNAPPS_DL_FILE
    fi
    tar -xzf $SYNAPPS_DL_FILE

    if [ -f "$SSCAN_DL_FILE" ]; then
        echo -e "${WARN}==> $SSCAN_DL_FILE already exists ${NC}"
    else 
        echo -e "${INFO}==> Downloading $SSCAN_DL_FILE ${NC}"
        wget https://github.com/epics-modules/sscan/archive/refs/tags/$SSCAN_VERSION.tar.gz -O $SSCAN_DL_FILE
    fi
    tar -xzf $SSCAN_DL_FILE

    if [ -f "$AREA_DETECTOR_FILE" ]; then
        echo -e "${WARN}==> $AREA_DETECTOR_FILE already exists ${NC}"
    else 
        echo -e "${INFO}==> Downloading $AREA_DETECTOR_FILE ${NC}"
        wget https://github.com/areaDetector/areaDetector/archive/refs/tags/$AREA_DETECTOR_VERSION.tar.gz -O $AREA_DETECTOR_FILE
    fi
    tar -xzf $AREA_DETECTOR_FILE

    if [ -f "$ADSUPPORT_FILE" ]; then
        echo -e "${WARN}==> $ADSUPPORT_FILE already exists ${NC}"
    else 
        echo -e "${INFO}==> Downloading $ADSUPPORT_FILE ${NC}"
        wget https://github.com/areaDetector/ADSupport/archive/refs/tags/$ADSUPPORT_VERSION.tar.gz -O $ADSUPPORT_FILE
    fi
    tar -xzf $ADSUPPORT_FILE

    if [ -f "$ADCORE_FILE" ]; then
        echo -e "${WARN}==> $ADCORE_FILE already exists ${NC}"
    else 
        echo -e "${INFO}==> Downloading $ADCORE_FILE ${NC}"
        wget https://github.com/areaDetector/ADCore/archive/refs/tags/$ADCORE_VERSION.tar.gz -O $ADCORE_FILE
    fi
    tar -xzf $ADCORE_FILE

    if [ -f "$ASYN_FILE" ]; then
        echo -e "${WARN}==> $ASYN_FILE already exists ${NC}"
    else 
        echo -e "${INFO}==> Downloading $ASYN_FILE ${NC}"
        wget https://github.com/epics-modules/asyn/archive/refs/tags/$ASYN_VERSION.tar.gz -O $ASYN_FILE
    fi
    tar -xzf $ASYN_FILE

    # wget https://github.com/epics-modules/motor/archive/refs/tags/R7-3-1.tar.gz -O motor-R7-3-1.tar.gz
    # tar -xzf motor-R7-3-1.tar.gz
    cd -
}

CompileEPICSBase() {
    echo -e "${INFO}==> Setting EPICS Base in $EPICS_INSTALL_PATH ${NC}"
    mv $DOWNLOADS_PATH/base-$EPICS_BASE_VERSION $EPICS_INSTALL_PATH/base
    cd $EPICS_INSTALL_PATH/base
    # Set the install location on EPICS CONFIG_SITE to be used by all dependencies
    sed -i "/^#INSTALL_LOCATION=/c\INSTALL_LOCATION=$EPICS_INSTALL_PATH/base" configure/CONFIG_SITE 

    echo -e "${INFO}==> Make EPICS BASE ${NC}"
    make -j6 -s
    cd -
}

CompileSynapps() {
    # See: https://areadetector.github.io/areaDetector/install_guide.html
    echo -e "${INFO}==> Preparing SynApps ${NC}"

    # Move new support modules
    mv $DOWNLOADS_PATH/synApps_6_1 $EPICS_INSTALL_PATH/synApps
    # mv motor-R7-3-1 /usr/local/epics/synApps/support
    mv $DOWNLOADS_PATH/sscan-$SSCAN_VERSION $EPICS_INSTALL_PATH/synApps/support    
    # Move areaDetector, ADSupport and ADCore
    mv $DOWNLOADS_PATH/areaDetector-$AREA_DETECTOR_VERSION $EPICS_INSTALL_PATH/synApps/support
    mv $DOWNLOADS_PATH/asyn-$ASYN_VERSION $EPICS_INSTALL_PATH/synApps/support/
    mv $DOWNLOADS_PATH/ADSupport-$ADSUPPORT_VERSION/* $EPICS_INSTALL_PATH/synApps/support/areaDetector-$AREA_DETECTOR_VERSION/ADSupport
    mv $DOWNLOADS_PATH/ADCore-$ADCORE_VERSION/* $EPICS_INSTALL_PATH/synApps/support/areaDetector-$AREA_DETECTOR_VERSION/ADCore

    # Copy ADPimega to areaDetector directory
    mkdir $ADPIMEGA_INSTALL_DIR
    rsync -av ../ $ADPIMEGA_INSTALL_DIR --exclude install --exclude test --exclude *.yaml --exclude *.yml

    # Update release files
    sed -i "/^SUPPORT=/c\SUPPORT=$EPICS_INSTALL_PATH/synApps/support/" RELEASE_synapps 
    sed -i "/EPICS_BASE=/c\EPICS_BASE=$EPICS_INSTALL_PATH/base/" RELEASE_synapps
    cp RELEASE_synapps $EPICS_INSTALL_PATH/synApps/support/configure/RELEASE
    # Set the EPICS_BASE variable for IPAC
    sed -i "/EPICS_BASE=/c\EPICS_BASE=$EPICS_INSTALL_PATH/base/" $EPICS_INSTALL_PATH/synApps/support/ipac-2-15/configure/RELEASE
    # Enable TIRPC for ASYN
    sed -i "/^# TIRPC/c\TIRPC = YES" $EPICS_INSTALL_PATH/synApps/support/asyn-$ASYN_VERSION/configure/CONFIG_SITE
    # Set the EPICS_BASE variable for ASYN
    sed -i "/#EPICS_BASE=/c\EPICS_BASE=$EPICS_INSTALL_PATH/base" $EPICS_INSTALL_PATH/synApps/support/asyn-$ASYN_VERSION/configure/RELEASE
    # Disable unit tests from ADCore
    sed -i "/^DIRS += pluginTests/c\#DIRS += pluginTests" $EPICS_INSTALL_PATH/synApps/support/areaDetector-$AREA_DETECTOR_VERSION/ADCore/ADApp/Makefile

    echo -e "${INFO}==> Setup release files ${NC}"    

    # This step updates all .local files with default areaDetector values
    cd $EPICS_INSTALL_PATH/synApps/support
    cd areaDetector-$AREA_DETECTOR_VERSION/configure/
    bash copyFromExample

    # Add ADPIMEGA to list of drivers that should be built
    echo 'ADPIMEGA=$(AREA_DETECTOR)/ADPimega' > RELEASE.local.linux-x86_64
    cd -

    # Update release files
    make release -s

    echo -e "${INFO}==> Build synApps Support ${NC}"    
    make -j4 -s
}

CompileADPimega() {

    make
}

echo -e "${INFO}==> Starting EPICS installation ${NC}"
CleanBeforeInstall
SetupInstaller
DownloadRequirements
CompileEPICSBase
CompileSynapps
# CompileADPimega
echo -e "${INFO}==> Done! ${NC}"
