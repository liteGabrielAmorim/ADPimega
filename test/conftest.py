"""Configuration file for AD Pimega tests."""
import os
import pytest
from epics import PV
from pytest import ExitCode


def pytest_addoption(parser):
    """Pytest command line arguments."""
    parser.addini("epics_prefix", help="EPICS Prefix")
    parser.addini("epics_camera", help="Area Detector Camera id")
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


@pytest.fixture(scope="session", name="pimega")
def ADPimega_PV(request):
    """Returns the EPICS prefix to access an equipment.
    This value is set on pytest.ini.
    """
    pimega = PV(request.config.getini("epics_prefix") + ":" + request.config.getini("epics_camera"))
    yield pimega
