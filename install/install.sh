#!/bin/bash
set -x
EPICS_BASE_VERSION='7.0.8'
INFO='\033[0;32m'
NC='\033[0m'

if [ "$EUID" -ne 0 ]
  then echo "This installer must be run as root"
  exit
fi

CleanBeforeInstall(){
    echo -e "${INFO}==> Removing existing EPICS installation folder ${NC}"
    rm -rf /usr/local/epics
}

SetupInstaller() {
    echo -e "${INFO}==> Copying items from data directory ${NC}"
    cp data/epics.sh /etc/profile.d/
    cp data/RELEASE /tmp/
    cp data/RELEASE_motor-r7-1 /tmp/
    cp data/RELEASE_ipac /tmp/
    echo -e "${INFO}==> Copying area detector source to /tmp/ADPimega/epics/ ${NC}"
    mkdir -p /tmp/ADPimega/epics/
    cp -r ../ /tmp/ADPimega/epics/
    chmod +x /etc/profile.d/epics.sh
    echo ". /etc/profile.d/epics.sh" >> /etc/bash.bashrc
    arch | xargs -i@ echo "/usr/local/epics/base/lib/linux-@" > /etc/ld.so.conf.d/epics.conf
    echo -e "${INFO}==> Creating EPICS install directory ${NC}"
    set +e
    mkdir /usr/local/epics
}

DownloadRequirements() {
    echo -e "${INFO}==> Downloading base-$EPICS_BASE_VERSION and synApps_6_1 ${NC}"
    cd /tmp
    wget https://epics.anl.gov/download/base/base-$EPICS_BASE_VERSION.tar.gz
    tar -xzf base-$EPICS_BASE_VERSION.tar.gz
    wget https://epics.anl.gov/bcda/synApps/tar/synApps_6_1.tar.gz
    tar -xzf synApps_6_1.tar.gz
    wget https://github.com/epics-modules/motor/archive/refs/tags/R7-3-1.tar.gz -O motor-R7-3-1.tar.gz
    tar -xzf motor-R7-3-1.tar.gz
}

CompileAll() {
    echo -e "${INFO}==> Copying source to /usr/local/epics ${NC}"
    mv base-$EPICS_BASE_VERSION /usr/local/epics/base
    mv synApps_6_1 /usr/local/epics/synApps
    mv motor-R7-3-1 /usr/local/epics/synApps/support
    mv RELEASE /usr/local/epics/synApps/support/configure/RELEASE
    mv RELEASE_motor-r7-1 /usr/local/epics/synApps/support/motor-R7-1/configure/RELEASE
    mv RELEASE_ipac /usr/local/epics/synApps/support/ipac-2-15/configure/RELEASE
    cd /usr/local/epics/base
    echo -e "${INFO}==> Make EPICS BASE ${NC}"
    make -j -s
    ln -s /usr/local/epics/base /usr/local/epics/base
    cd /usr/local/epics/synApps/support
    echo -e "${INFO}==> Make synApps Support ${NC}"
    make release -s
    make -s
    mv /tmp/ADPimega /usr/local/epics/synApps/support/areaDetector-R3-7/
}

echo -e "${INFO}==> Starting EPICS installation ${NC}"
CleanBeforeInstall
SetupInstaller
DownloadRequirements
CompileAll
echo -e "${INFO}==> Done! ${NC}"
