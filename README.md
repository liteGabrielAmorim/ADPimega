# PIMEGA areaDetector IOC

This is an IOC for the PIMEGA area detector models 45D, 135D, 540D, 450D and 450DS.
It must be included in compiled in the areaDetector folder of synApps.

## Dependencies

This IOC requires the PIMEGA library to be installed in /usr/lib/ under libpimega.so.
The include files must be added to /usr/local/include/pimega.

## Build

Add this repository content to areaDetector/ADPimega and run the Makefile:

```
$ cd ADPimega
$ make
```

## Run
To start and IOC, enter the iocPimega directory and execute the .cmd file that contains the PIMEGA model on its filename.
```
$ cd iocs/pimegaIOC/iocBoot/iocPimega
$ ./st-pitec-d-pimega<model>.cmd
```

## Test
To execute tests, first you need the requirements listed on `requirements-dev.txt`. Create a Python virtual environment and install those requirements.

When installed, just invoke `pytest` with the virtual environment active.
To enable verbose output, call `pytest -s`.

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements-dev.txt
$ pytest -s .  # -> Run this to start the test
```

__Important__: use the file `test/pytest.ini` to set custom EPICS and pytest configuration, if necessary.
