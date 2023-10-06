"Acquisition PVs abstraction "

import pytest


@pytest.fixture()
def acquire_mode(init_pv, dev_id):
    """ Acquisition mode PV """
    return init_pv[dev_id]["system"]["MedipixMode"]


@pytest.fixture()
def acquire_mode_rbv(init_pv, dev_id):
    """ RBV Acquisition mode PV """
    return init_pv[dev_id]["system"]["MedipixMode_RBV"]
