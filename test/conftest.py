"""Configuration file for AD Pimega tests."""
import json
import os
from types import SimpleNamespace

import pytest

from epics import PV

from .utils import (number_of_chips, number_of_modules, number_of_dacs,
                    number_of_boards, number_of_image_patterns, get_detector_read_out_by_counter)
from .pv.acquisition import *
from .pv.dac import *
from .pv.omr import *
from .pv.system import *
from .pv.filesystem import *
from .pv.status import *


def pytest_addoption(parser):
    """Pytest command line arguments."""
    parser.addini("epics_prefix", help="EPICS Prefix")
    parser.addini("device_id", help="Area Detector Camera id")
    parser.addini("epics_ip", help="IP Address to connect")
    parser.addini("detector_model", help="Detector model")
    parser.addini("minimal_gap", help="Minimal gap for the acquisition")


def pytest_configure(config):
    """Allow plugins and conftest files to perform initial configuration.
       Configure the Pytest environment before test starts."""
    if "EPICS_CA_ADDR_LIST" in os.environ:
        os.environ["EPICS_CA_ADDR_LIST"] += " " + config.getini("epics_ip")
    else:
        os.environ["EPICS_CA_ADDR_LIST"] = config.getini("epics_ip")

    # using the alternative to the deprecated pytest_namespace
    # https://docs.pytest.org/en/latest/deprecations.html#pytest-namespace
    pytest.config = SimpleNamespace()
    pytest.config.readout_counter = get_detector_read_out_by_counter(config)
    pytest.config.chips_total = number_of_chips(config)
    pytest.config.modules_total = number_of_modules(config)
    pytest.config.dacs_total = number_of_dacs()
    pytest.config.boards_total = number_of_boards(config)
    pytest.config.images_patterns_total = number_of_image_patterns()


def pytest_unconfigure(config):
    """Called before test process is exited."""


@pytest.fixture(scope="session", autouse=True)
def init_pv(request):
    """ Initialize the EPICS PVs """
    with open("PVs.json", "r", encoding="utf8") as cfg_file:
        pvs_config = json.load(cfg_file)

    epics_prefix = request.config.getini("epics_prefix")
    pvs_dict = {}
    for ad_type in pvs_config:
        pvs_dict[ad_type] = {}
        for pv_functionality in pvs_config[ad_type]:
            pvs_dict[ad_type][pv_functionality] = {}
            for pv_method in pvs_config[ad_type][pv_functionality]:
                pv_name = "{}:{}:{}".format(epics_prefix, ad_type, pv_method)
                pvs_dict[ad_type][pv_functionality][pv_method] = PV(pv_name)
    yield pvs_dict


@pytest.fixture(scope="session", name="dev_id")
def get_detector_epics_id(request):
    """ Get the EPICS device id """
    return request.config.getini("device_id")


@pytest.fixture(scope="session", name="minimal_gap")
def get_detector_minimal_gap(request):
    """
    Get the detector minimal_gap
    Note: As the API condition is for higer/lower or equal, 1 micro seconds is added
    """
    api_conditional_increment = 1e-6
    return float(request.config.getini("minimal_gap")) + api_conditional_increment
