import pytest

@pytest.fixture()
def continuousrw_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["ContinuousRW"]


@pytest.fixture()
def continuousrw_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["ContinuousRW_RBV"]


@pytest.fixture()
def counterdepth_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["CounterDepth"]


@pytest.fixture()
def counterdepth_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["CounterDepth_RBV"]


@pytest.fixture()
def discriminator_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["Discriminator"]


@pytest.fixture()
def discriminator_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["Discriminator_RBV"]


@pytest.fixture()
def equalization_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["Equalization"]


@pytest.fixture()
def equalization_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["Equalization_RBV"]


@pytest.fixture()
def extbgsel_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["ExtBgSel"]


@pytest.fixture()
def extbgsel_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["ExtBgSel_RBV"]


@pytest.fixture()
def gainmode_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["GainMode"]


@pytest.fixture()
def gainmode_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["GainMode_RBV"]


@pytest.fixture()
def omromselec_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["OmrOMSelec"]


@pytest.fixture()
def omromselec_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["OmrOMSelec_RBV"]


@pytest.fixture()
def pixelmode_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["PixelMode"]


@pytest.fixture()
def pixelmode_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["PixelMode_RBV"]


@pytest.fixture()
def polarity_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["Polarity"]


@pytest.fixture()
def polarity_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["Polarity_RBV"]


@pytest.fixture()
def testpulse_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["TestPulse"]


@pytest.fixture()
def testpulse_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["omr"]["TestPulse_RBV"]
