#!/bin/bash
# PIMEGA Area Detector testing system
# Pi-Tecnologia @Lumentum, 2023

Help()
{
  # Display Help
  echo
  echo " Run EPICS tests"
  echo
  echo " usage: ./run_test.sh [option]"
  echo
  echo " option:"
  echo "      --unit       or -u : Install the CLI with common user commands"
  echo "      --functional or -f : Install the CLI with advanced user commands"
  echo "      --production or -p : Install the CLI with production commands"
  echo "      --help       or -h : Show help information"
}

if [[ $@ == "--help" ]] || [[ $@ == "-h" ]] || [[ -z $@ ]]; then
    Help
    exit 0
fi

source venv_epics_test/bin/activate

if [ $@ == "--unit" ] || [ $@ == "-u" ]; then
    pytest -m unit_test
elif [ $@ == "--functional" ] || [ $@ == "-f" ]; then
    pytest -m unit_functional
elif [ $@ == "--production" ] || [ $@ == "-p" ]; then
    pytest -m unit_production
else
    pytest
fi
