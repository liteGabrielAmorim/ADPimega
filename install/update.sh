#!/bin/bash
set -x

if [ "$EUID" -ne 0 ]
  then echo "This installer must be run as root"
  exit
fi

rm -rf /usr/local/epics/synApps/support/areaDetector-R3-7/ADPimega
cp -r ../../epics /usr/local/epics/synApps/support/areaDetector-R3-7/ADPimega
cd $PIMEGA_PSS/api
bash build.sh -e
cd /usr/local/epics/synApps/support/areaDetector-R3-7/ADPimega
make
cd iocs
make
cd pimegaIOC
make
cd iocBoot
make
