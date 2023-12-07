"""
Basic PVs for status tests
"""
import pytest


@pytest.fixture()
def iocstatusmessage_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["status"]["IOCStatusMessage_RBV"]


@pytest.fixture()
def detstatusmessage_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["status"]["DetectorState_RBV"]


@pytest.fixture()
def time_remaining_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["status"]["TimeRemaining_RBV"]


@pytest.fixture()
def images_received_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["status"]["NumImagesCounter_RBV"]


@pytest.fixture()
def images_processed_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["status"]["ProcessedAcquisitionCounter_RBV"]


@pytest.fixture()
def images_saved_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["status"]["NumCaptured_RBV"]
