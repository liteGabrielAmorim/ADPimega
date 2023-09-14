"""Configuration file for AD Pimega tests."""
import json
import os

import pytest

from epics import PV


def pytest_addoption(parser):
    """Pytest command line arguments."""
    parser.addini("epics_prefix", help="EPICS Prefix")
    parser.addini("device_id", help="Area Detector Camera id")
    parser.addini("epics_ip", help="IP Address to connect")


def pytest_configure(config):
    """Allow plugins and conftest files to perform initial configuration.
       Configure the Pytest environment before test starts."""
    if "EPICS_CA_ADDR_LIST" in os.environ:
        os.environ["EPICS_CA_ADDR_LIST"] += " " + config.getini("epics_ip")
    else:
        os.environ["EPICS_CA_ADDR_LIST"] = config.getini("epics_ip")


def pytest_unconfigure(config):
    """Called before test process is exited."""


@pytest.fixture(scope="session", autouse=True)
def init_pv(request):
    """ Initialize the EPICS PVs """
    with open("PVs.json", "r", encoding="utf8") as cfg_file:
        pvs_dict = json.load(cfg_file)

    for ad_type in list(pvs_dict.keys()):
        for pv_functionality in list(pvs_dict[ad_type].keys()):
            for pv_method in list(pvs_dict[ad_type][pv_functionality].keys()):
                pvs_dict[ad_type][pv_functionality][pv_method] = PV(
                    request.config.getini("epics_prefix") + ":" + ad_type + ":" + pv_method)
    yield pvs_dict


@pytest.fixture(scope="session", name="dev_id")
def get_detector_epics_id(request):
    """ Get the EPICS device id """
    return request.config.getini("device_id")


# ----------- Acquisition PVs abstraction -----------
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
def numexp(init_pv, dev_id):
    """ numexp PV """
    return init_pv[dev_id]["acquisition"]["NumExposures"]


@pytest.fixture()
def numexp_rbv(init_pv, dev_id):
    """ RBV numexp PV """
    return init_pv[dev_id]["acquisition"]["NumExposures_RBV"]


@pytest.fixture()
def numcap(init_pv, dev_id):
    """ number of captures PV """
    return init_pv[dev_id]["acquisition"]["NumCapture"]


@pytest.fixture()
def numcap_rbv(init_pv, dev_id):
    """ RBV number of captures PV """
    return init_pv[dev_id]["acquisition"]["NumCapture_RBV"]
