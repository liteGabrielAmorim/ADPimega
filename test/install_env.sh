#!/bin/bash
# PIMEGA Area Detector testing system
# Pi-Tecnologia @Lumentum, 2023

echo "PIMEGA Area Detector testing system"

python3 -m venv venv_epics_test

source "venv_epics_test/bin/activate"
pip3 install pytest>=7
pip3 install pyepics

deactivate
