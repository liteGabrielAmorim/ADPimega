import pytest


@pytest.fixture()
def acq_time(init_pv, dev_id):
    return init_pv[dev_id]["acquisition"]["AcquireTime"]


@pytest.fixture()
def acq_time_rbv(init_pv, dev_id):
    return init_pv[dev_id]["acquisition"]["AcquireTime_RBV"]
