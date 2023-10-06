import pytest


@pytest.mark.parametrize("continuousrw", [0, 1])
def test_continuousrw(continuousrw_pv, continuousrw_rbv_pv, continuousrw):
    """ Test continuousrw (positive tests) """
    continuousrw_pv.put(continuousrw, wait=True)
    ans = continuousrw_rbv_pv.get(use_monitor=False)
    print(f"Value set: {continuousrw}; | Value read: {ans}")
    assert ans == bool(continuousrw)


@pytest.mark.parametrize("continuousrw", [-1, 2])
def test_continuousrw_invalid_range(continuousrw_pv, continuousrw_rbv_pv, continuousrw):
    """ Test continuousrw (invalid tests) """
    continuousrw_pv.put(continuousrw, wait=True)
    ans = continuousrw_rbv_pv.get(use_monitor=False)
    print(f"Value set: {continuousrw} | Value read: {ans}")
    assert ans == bool(continuousrw)


@pytest.mark.parametrize("counterdepth", [0, 1, 2, 3])
def test_counterdepth(counterdepth_pv, counterdepth_rbv_pv, counterdepth):
    """ Test counterdepth (positive tests) """
    counterdepth_pv.put(counterdepth, wait=True)
    ans = counterdepth_rbv_pv.get(use_monitor=False)
    print(f"Value set: {counterdepth}; | Value read: {ans}")
    assert ans == counterdepth


@pytest.mark.parametrize("counterdepth", [-1, -255, 256])
def test_counterdepth_invalid_range(counterdepth_pv, counterdepth_rbv_pv, counterdepth):
    """ Test counterdepth (invalid tests) """
    valid_range = (0, 255)
    counterdepth_pv.put(counterdepth, wait=True)
    ans = counterdepth_rbv_pv.get(use_monitor=False)
    print(f"Value set: {counterdepth} | Value read: {ans}")
    assert ans == min(max(counterdepth, valid_range[0]), valid_range[1])


@pytest.mark.parametrize("discriminator", [0, 1, 255])
def test_discriminator(discriminator_pv, discriminator_rbv_pv, discriminator):
    """ Test discriminator (positive tests) """
    discriminator_pv.put(discriminator, wait=True)
    ans = discriminator_rbv_pv.get(use_monitor=False)
    print(f"Value set: {discriminator}; | Value read: {ans}")
    assert ans == discriminator


@pytest.mark.parametrize("discriminator", [-1, -255, 256])
def test_discriminator_invalid_range(discriminator_pv, discriminator_rbv_pv, discriminator):
    """ Test discriminator (invalid tests) """
    valid_range = (0, 255)
    discriminator_pv.put(discriminator, wait=True)
    ans = discriminator_rbv_pv.get(use_monitor=False)
    print(f"Value set: {discriminator} | Value read: {ans}")
    assert ans == min(max(discriminator, valid_range[0]), valid_range[1])


@pytest.mark.parametrize("equalization", [0, 1])
def test_equalization(equalization_pv, equalization_rbv_pv, equalization):
    """ Test equalization (positive tests) """
    equalization_pv.put(equalization, wait=True)
    ans = equalization_rbv_pv.get(use_monitor=False)
    print(f"Value set: {equalization}; | Value read: {ans}")
    assert ans == bool(equalization)


@pytest.mark.parametrize("equalization", [-1, -255, 256])
def test_equalization_invalid_range(equalization_pv, equalization_rbv_pv, equalization):
    """ Test equalization (invalid tests) """
    equalization_pv.put(equalization, wait=True)
    ans = equalization_rbv_pv.get(use_monitor=False)
    print(f"Value set: {equalization} | Value read: {ans}")
    assert ans == bool(equalization)


@pytest.mark.parametrize("extbgsel", [0, 1])
def test_extbgsel(extbgsel_pv, extbgsel_rbv_pv, extbgsel):
    """ Test extbgsel (positive tests) """
    extbgsel_pv.put(extbgsel, wait=True)
    ans = extbgsel_rbv_pv.get(use_monitor=False)
    print(f"Value set: {extbgsel}; | Value read: {ans}")
    assert ans == bool(extbgsel)


@pytest.mark.parametrize("extbgsel", [-1, 2])
def test_extbgsel_invalid_range(extbgsel_pv, extbgsel_rbv_pv, extbgsel):
    """ Test extbgsel (invalid tests) """
    extbgsel_pv.put(extbgsel, wait=True)
    ans = extbgsel_rbv_pv.get(use_monitor=False)
    print(f"Value set: {extbgsel} | Value read: {ans}")
    assert ans == bool(extbgsel)


@pytest.mark.parametrize("gainmode", [0, 1, 2, 3])
def test_gainmode(gainmode_pv, gainmode_rbv_pv, gainmode):
    """ Test gainmode (positive tests) """
    gainmode_pv.put(gainmode, wait=True)
    ans = gainmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {gainmode}; | Value read: {ans}")
    assert ans == gainmode


@pytest.mark.parametrize("gainmode", [-1, 4])
def test_gainmode_invalid_range(gainmode_pv, gainmode_rbv_pv, gainmode):
    """ Test gainmode (invalid tests) """
    valid_range = (0, 3)
    gainmode_pv.put(gainmode, wait=True)
    ans = gainmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {gainmode} | Value read: {ans}")
    assert ans == min(max(gainmode, valid_range[0]), valid_range[1])


@pytest.mark.parametrize("omromselec", [0, 1, 2, 3, 4, 5, 6, 7])
def test_omromselec(omromselec_pv, omromselec_rbv_pv, omromselec):
    """ Test omromselec (positive tests) """
    omromselec_pv.put(omromselec, wait=True)
    ans = omromselec_rbv_pv.get(use_monitor=False)
    print(f"Value set: {omromselec}; | Value read: {ans}")
    assert ans == omromselec


@pytest.mark.parametrize("omromselec", [-1, 8])
def test_omromselec_invalid_range(omromselec_pv, omromselec_rbv_pv, omromselec):
    """ Test omromselec (invalid tests) """
    omromselec_pv.put(omromselec, wait=True)
    valid_range = (0, 7)
    ans = omromselec_rbv_pv.get(use_monitor=False)
    print(f"Value set: {omromselec} | Value read: {ans}")
    assert ans == min(max(omromselec, valid_range[0]), valid_range[1])


@pytest.mark.parametrize("pixelmode", [0, 1])
def test_pixelmode(pixelmode_pv, pixelmode_rbv_pv, pixelmode):
    """ Test pixelmode (positive tests) """
    pixelmode_pv.put(pixelmode, wait=True)
    ans = pixelmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {pixelmode}; | Value read: {ans}")
    assert ans == pixelmode


@pytest.mark.parametrize("pixelmode", [-1, 2])
def test_pixelmode_invalid_range(pixelmode_pv, pixelmode_rbv_pv, pixelmode):
    """ Test pixelmode (invalid tests) """
    pixelmode_pv.put(pixelmode, wait=True)
    valid_range = (0, 1)
    ans = pixelmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {pixelmode} | Value read: {ans}")
    assert ans == min(max(pixelmode, valid_range[0]), valid_range[1])


@pytest.mark.parametrize("polarity", [0, 1])
def test_polarity(polarity_pv, polarity_rbv_pv, polarity):
    """ Test polarity (positive tests) """
    polarity_pv.put(polarity, wait=True)
    ans = polarity_rbv_pv.get(use_monitor=False)
    print(f"Value set: {polarity}; | Value read: {ans}")
    assert ans == polarity


@pytest.mark.parametrize("polarity", [-1, 2])
def test_polarity_invalid_range(polarity_pv, polarity_rbv_pv, polarity):
    """ Test polarity (invalid tests) """
    polarity_pv.put(polarity, wait=True) 
    valid_range = (0, 1)
    ans = polarity_rbv_pv.get(use_monitor=False)
    print(f"Value set: {polarity} | Value read: {ans}")
    assert ans == min(max(polarity, valid_range[0]), valid_range[1])


@pytest.mark.parametrize("testpulse", [0, 1])
def test_testpulse(testpulse_pv, testpulse_rbv_pv, testpulse):
    """ Test testpulse (positive tests) """
    testpulse_pv.put(testpulse, wait=True)
    ans = testpulse_rbv_pv.get(use_monitor=False)
    print(f"Value set: {testpulse}; | Value read: {ans}")
    assert ans == bool(testpulse)


@pytest.mark.parametrize("testpulse", [-1, 2])
def test_testpulse_invalid_range(testpulse_pv, testpulse_rbv_pv, testpulse):
    """ Test testpulse (invalid tests) """
    testpulse_pv.put(testpulse, wait=True)
    ans = testpulse_rbv_pv.get(use_monitor=False)
    print(f"Value set: {testpulse} | Value read: {ans}")
    assert ans == bool(testpulse)
