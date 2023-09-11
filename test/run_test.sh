#!/bin/bash
# PIMEGA Area Detector testing system
# Pi-Tecnologia @Lumentum, 2023

source venv_epics_test/bin/activate
pytest
deactivate
