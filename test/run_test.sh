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
  echo "      --all        or -a : Run all the tests"
  echo "      --unit       or -u : Run the unit tests"
  echo "      --functional or -f : Run the functional tests"
  echo "      --production or -p : Run the production tests"
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
elif [ $@ == "--all" ] || [ $@ == "-a" ]; then
    pytest
fi
