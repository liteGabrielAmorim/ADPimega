import pytest


@pytest.fixture()
def dac_cas_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_CAS"]


@pytest.fixture()
def dac_cas_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_CAS_RBV"]


@pytest.fixture()
def dac_delay_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_Delay"]


@pytest.fixture()
def dac_delay_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_Delay_RBV"]


@pytest.fixture()
def dac_disc_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_Disc"]


@pytest.fixture()
def dac_disch_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_DiscH"]


@pytest.fixture()
def dac_disch_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_DiscH_RBV"]


@pytest.fixture()
def dac_discl_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_DiscL"]


@pytest.fixture()
def dac_discls_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_DiscLS"]


@pytest.fixture()
def dac_discls_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_DiscLS_RBV"]


@pytest.fixture()
def dac_discl_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_DiscL_RBV"]


@pytest.fixture()
def dac_disc_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_Disc_RBV"]


@pytest.fixture()
def dac_fbk_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_FBK"]


@pytest.fixture()
def dac_fbk_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_FBK_RBV"]


@pytest.fixture()
def dac_gnd_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_GND"]


@pytest.fixture()
def dac_gnd_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_GND_RBV"]


@pytest.fixture()
def dac_ikrum_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_IKrum_RBV"]


@pytest.fixture()
def dac_ikrum_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_IKrum"]


@pytest.fixture()
def dac_preamp_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_Preamp"]


@pytest.fixture()
def dac_preamp_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_Preamp_RBV"]


@pytest.fixture()
def dac_rpz_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_RPZ"]


@pytest.fixture()
def dac_rpz_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_RPZ_RBV"]


@pytest.fixture()
def dac_shaper_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_Shaper"]


@pytest.fixture()
def dac_shaper_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_Shaper_RBV"]


@pytest.fixture()
def dac_tpbufferin_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPBufferIn"]


@pytest.fixture()
def dac_tpbufferin_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPBufferIn_RBV"]


@pytest.fixture()
def dac_tpbufferout_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPBufferOut"]


@pytest.fixture()
def dac_tpbufferout_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPBufferOut_RBV"]


@pytest.fixture()
def dac_tpref_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPRef"]


@pytest.fixture()
def dac_tprefa_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPRefA"]


@pytest.fixture()
def dac_tprefa_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPRefA_RBV"]


@pytest.fixture()
def dac_tprefb_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPRefB"]


@pytest.fixture()
def dac_tprefb_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPRefB_RBV"]


@pytest.fixture()
def dac_tpref_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_TPRef_RBV"]


@pytest.fixture()
def dac_thresholdenergy0_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy0"]


@pytest.fixture()
def dac_thresholdenergy0_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy0_RBV"]


@pytest.fixture()
def dac_thresholdenergy1_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1"]


@pytest.fixture()
def dac_thresholdenergy1_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1_RBV"]


@pytest.fixture()
def dac_thresholdenergy2_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy0"]


@pytest.fixture()
def dac_thresholdenergy2_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy0_RBV"]


@pytest.fixture()
def dac_thresholdenergy3_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1"]


@pytest.fixture()
def dac_thresholdenergy3_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1_RBV"]


@pytest.fixture()
def dac_thresholdenergy4_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1"]


@pytest.fixture()
def dac_thresholdenergy4_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1_RBV"]


@pytest.fixture()
def dac_thresholdenergy5_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1"]


@pytest.fixture()
def dac_thresholdenergy5_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1_RBV"]


@pytest.fixture()
def dac_thresholdenergy6_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1"]


@pytest.fixture()
def dac_thresholdenergy6_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1_RBV"]


@pytest.fixture()
def dac_thresholdenergy7_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1"]


@pytest.fixture()
def dac_thresholdenergy7_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["DAC_ThresholdEnergy1_RBV"]


@pytest.fixture()
def senddac_done_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["dac"]["SendDAC_Done_RBV"]
