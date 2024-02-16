#!/bin/bash
set -e

if [ "$EUID" -ne 0 ]
  then echo "This installer must be run as root"
  exit 1
fi

if [ -z "${PIMEGA_PSS}" ]; then
    echo "PIMEGA_PSS is not set"
    exit 1
else
    echo "PIMEGA_PSS: $PIMEGA_PSS"
fi

rm -rf /usr/local/epics/synApps/support/areaDetector-R3-7/ADPimega
cp -r ../ /usr/local/epics/synApps/support/areaDetector-R3-7/ADPimega
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
