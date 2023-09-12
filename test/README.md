# Pimega area detector IOC test

The declaration of the EPICS prefix, camera id, and IP where the EPICS Driver is initialized, is
done at the file pytest.ini.

To declare a new PV to be tested, declare it in the file PVs.json (always start it as None), and
in the the respective file inside of the folder PVs, declare the method that will return the result
of the PV.

It is required to run the test from the test directory