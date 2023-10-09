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


@pytest.fixture()
def allmodules_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["AllModules"]


@pytest.fixture()
def allmodules_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["AllModules_RBV"]


@pytest.fixture()
def dacoutsense_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["DacOutSense_RBV"]


@pytest.fixture()
def extbgin_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["ExtBgIn"]


@pytest.fixture()
def extbgin_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["ExtBgIn_RBV"]


@pytest.fixture()
def imgchipnumberid_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["ImgChipNumberID"]


@pytest.fixture()
def imgchipnumberid_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["ImgChipNumberID_RBV"]


@pytest.fixture()
def loadequalization_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["LoadEqualization"]


@pytest.fixture()
def loadequalizationstart_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["LoadEqualizationStart"]


@pytest.fixture()
def mb_sendmode_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["MB_SendMode"]


@pytest.fixture()
def mb_sendmode_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["MB_SendMode_RBV"]


@pytest.fixture()
def medipixboard_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["MedipixBoard"]


@pytest.fixture()
def medipixboard_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["MedipixBoard_RBV"]


@pytest.fixture()
def pimegamodule_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["PimegaModule"]


@pytest.fixture()
def pimegamodule_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["PimegaModule_RBV"]


@pytest.fixture()
def reset_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["Reset"]


@pytest.fixture()
def reset_rdma_buffer_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["Reset_RDMA_Buffer"]


@pytest.fixture()
def reset_rdma_buffer_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["Reset_RDMA_Buffer_RBV"]


@pytest.fixture()
def select_sendimage_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["Select_SendImage"]


@pytest.fixture()
def sendimage_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["SendImage"]


@pytest.fixture()
def sensedacsel_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["SenseDacSel"]


@pytest.fixture()
def sensedacsel_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["SenseDacSel_RBV"]


@pytest.fixture()
def sensorbias_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["SensorBias"]


@pytest.fixture()
def sensorbias_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["SensorBias_RBV"]


@pytest.fixture()
def thresholdenergy_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["ThresholdEnergy"]


@pytest.fixture()
def thresholdenergy_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["ThresholdEnergy_RBV"]


@pytest.fixture()
def triggermode_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["TriggerMode"]


@pytest.fixture()
def triggermode_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["TriggerMode_RBV"]


@pytest.fixture()
def efuseid_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["system"]["eFuseID_RBV"]
