"Acquisition PVs abstraction "

from time import sleep

import pytest


@pytest.fixture()
def acq_time(init_pv, dev_id):
    """ Acquisition PV """
    return init_pv[dev_id]["acquisition"]["AcquireTime"]


@pytest.fixture()
def acq_time_rbv(init_pv, dev_id):
    """ RBV Acquisition PV """
    return init_pv[dev_id]["acquisition"]["AcquireTime_RBV"]


@pytest.fixture()
def acq_period(init_pv, dev_id):
    """ Period PV """
    return init_pv[dev_id]["acquisition"]["AcquirePeriod"]


@pytest.fixture()
def acq_period_rbv(init_pv, dev_id):
    """ RBV Period PV """
    return init_pv[dev_id]["acquisition"]["AcquirePeriod_RBV"]


@pytest.fixture()
def acquire(init_pv, dev_id):
    """ Start acquisition (detector side) PV """
    return init_pv[dev_id]["acquisition"]["Acquire"]


@pytest.fixture()
def capture(init_pv, dev_id):
    """ Start capture (backend side) PV """
    return init_pv[dev_id]["acquisition"]["Capture"]


@pytest.fixture()
def capture_rbv(init_pv, dev_id):
    """ Return of the capture PV """
    return init_pv[dev_id]["acquisition"]["Capture_RBV"]


@pytest.fixture()
def frame_processed_mode(init_pv, dev_id):
    """ Frame Processed mode PV """
    return init_pv[dev_id]["acquisition"]["FrameProcessMode"]


@pytest.fixture()
def numcap(init_pv, dev_id):
    """ number of captures PV """
    return init_pv[dev_id]["acquisition"]["NumCapture"]


@pytest.fixture()
def numcap_rbv(init_pv, dev_id):
    """ RBV number of captures PV """
    return init_pv[dev_id]["acquisition"]["NumCapture_RBV"]


@pytest.fixture()
def numexp(init_pv, dev_id):
    """ numexp PV """
    return init_pv[dev_id]["acquisition"]["NumExposures"]


@pytest.fixture()
def numexp_rbv(init_pv, dev_id):
    """ RBV numexp PV """
    return init_pv[dev_id]["acquisition"]["NumExposures_RBV"]
