import pytest


@pytest.fixture()
def iocstatusmessage_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["status"]["IOCStatusMessage_RBV"]


