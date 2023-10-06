import pytest


@pytest.mark.parametrize("dac_cas", [0, 1, 255])
def test_dac_cas(dac_cas_pv, dac_cas_rbv_pv, dac_cas):
    """ Test dac_cas (positive tests) """
    dac_cas_pv.put(dac_cas, wait=True)
    ans = dac_cas_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_cas}; | Value read: {ans}")
    assert ans == dac_cas


@pytest.mark.parametrize("dac_cas", [-1, -255, 256])
def test_dac_cas_invalid_range(dac_cas_pv, dac_cas_rbv_pv, dac_cas):
    """ Test dac_cas (invalid tests) """
    valid_range = (0, 255)
    dac_cas_pv.put(dac_cas, wait=True)
    ans = dac_cas_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_cas} | Value read: {ans}")
    assert ans == min(max(dac_cas, valid_range[0]), valid_range[1])


@pytest.mark.parametrize("dac_delay", [0, 1, 255])
def test_dac_delay(dac_delay_pv, dac_delay_rbv_pv, dac_delay):
    """ Test dac_delay (positive tests) """
    dac_delay_pv.put(dac_delay, wait=True)
    ans = dac_delay_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_delay}; | Value read: {ans}")
    assert ans == dac_delay


@pytest.mark.parametrize("dac_delay", [-1, -255, 256])
def test_dac_delay_invalid_range_max(dac_delay_pv, dac_delay_rbv_pv, dac_delay):
    """ Test dac_delay (invalid tests) """
    prev_value = dac_delay_rbv_pv.get(use_monitor=False)
    dac_delay_pv.put(dac_delay, wait=True)
    ans = dac_delay_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_delay} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_disc", [0, 1, 255])
def test_dac_disc(dac_disc_pv, dac_disc_rbv_pv, dac_disc):
    """ Test dac_disc (positive tests) """
    dac_disc_pv.put(dac_disc, wait=True)
    ans = dac_disc_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_disc}; | Value read: {ans}")
    assert ans == dac_disc


@pytest.mark.parametrize("dac_disc", [-1, -255, 256])
def test_dac_disc_invalid_range(dac_disc_pv, dac_disc_rbv_pv, dac_disc):
    """ Test dac_disc (invalid tests) """
    prev_value = dac_disc_rbv_pv.get(use_monitor=False)
    dac_disc_pv.put(dac_disc, wait=True)
    ans = dac_disc_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_disc} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_disch", [0, 1, 255])
def test_dac_disch(dac_disch_pv, dac_disch_rbv_pv, dac_disch):
    """ Test dac_disch (positive tests) """
    dac_disch_pv.put(dac_disch, wait=True)
    ans = dac_disch_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_disch}; | Value read: {ans}")
    assert ans == dac_disch


@pytest.mark.parametrize("dac_disch", [-1, -255, 256])
def test_dac_disch_invalid_range(dac_disch_pv, dac_disch_rbv_pv, dac_disch):
    """ Test dac_disch (invalid tests) """
    prev_value = dac_disch_rbv_pv.get(use_monitor=False)
    dac_disch_pv.put(dac_disch, wait=True)
    ans = dac_disch_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_disch} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_discl", [0, 1, 255])
def test_dac_discl(dac_discl_pv, dac_discl_rbv_pv, dac_discl):
    """ Test dac_discl (positive tests) """
    dac_discl_pv.put(dac_discl, wait=True)
    ans = dac_discl_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_discl}; | Value read: {ans}")
    assert ans == dac_discl


@pytest.mark.parametrize("dac_discl", [-1, -255, 256])
def test_dac_discl_invalid_range(dac_discl_pv, dac_discl_rbv_pv, dac_discl):
    """ Test dac_discl (invalid tests) """
    prev_value = dac_discl_rbv_pv.get(use_monitor=False)
    dac_discl_pv.put(dac_discl, wait=True)
    ans = dac_discl_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_discl} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_discls", [0, 1, 255])
def test_dac_discls(dac_discls_pv, dac_discls_rbv_pv, dac_discls):
    """ Test dac_discls (positive tests) """
    dac_discls_pv.put(dac_discls, wait=True)
    ans = dac_discls_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_discls}; | Value read: {ans}")
    assert ans == dac_discls


@pytest.mark.parametrize("dac_discls", [-1, -255, 256])
def test_dac_discls_invalid_range(dac_discls_pv, dac_discls_rbv_pv,
                                  dac_discls):
    """ Test dac_discls (invalid tests) """
    prev_value = dac_discls_rbv_pv.get(use_monitor=False)
    dac_discls_pv.put(dac_discls, wait=True)
    ans = dac_discls_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_discls} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_fbk", [0, 1, 255])
def test_dac_fbk(dac_fbk_pv, dac_fbk_rbv_pv, dac_fbk):
    """ Test dac_fbk (positive tests) """
    dac_fbk_pv.put(dac_fbk, wait=True)
    ans = dac_fbk_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_fbk}; | Value read: {ans}")
    assert ans == dac_fbk


@pytest.mark.parametrize("dac_fbk", [-1, -255, 256])
def test_dac_fbk_invalid_range(dac_fbk_pv, dac_fbk_rbv_pv, dac_fbk):
    """ Test dac_fbk (invalid tests) """
    prev_value = dac_fbk_rbv_pv.get(use_monitor=False)
    dac_fbk_pv.put(dac_fbk, wait=True)
    ans = dac_fbk_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_fbk} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_gnd", [0, 1, 255])
def test_dac_gnd(dac_gnd_pv, dac_gnd_rbv_pv, dac_gnd):
    """ Test dac_gnd (positive tests) """
    dac_gnd_pv.put(dac_gnd, wait=True)
    ans = dac_gnd_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_gnd}; | Value read: {ans}")
    assert ans == dac_gnd


@pytest.mark.parametrize("dac_gnd", [-1, -255, 256])
def test_dac_gnd_invalid_range(dac_gnd_pv, dac_gnd_rbv_pv, dac_gnd):
    """ Test dac_gnd (invalid tests) """
    prev_value = dac_gnd_rbv_pv.get(use_monitor=False)
    dac_gnd_pv.put(dac_gnd, wait=True)
    ans = dac_gnd_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_gnd} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_ikrum", [0, 1, 255])
def test_dac_ikrum(dac_ikrum_pv, dac_ikrum_rbv_pv, dac_ikrum):
    """ Test dac_ikrum (positive tests) """
    dac_ikrum_pv.put(dac_ikrum, wait=True)
    ans = dac_ikrum_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_ikrum}; | Value read: {ans}")
    assert ans == dac_ikrum


@pytest.mark.parametrize("dac_ikrum", [-1, -255, 256])
def test_dac_ikrum_invalid_range(dac_ikrum_pv, dac_ikrum_rbv_pv, dac_ikrum):
    """ Test dac_ikrum (invalid tests) """
    prev_value = dac_ikrum_rbv_pv.get(use_monitor=False)
    dac_ikrum_pv.put(dac_ikrum, wait=True)
    ans = dac_ikrum_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_ikrum} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_preamp", [0, 1, 255])
def test_dac_preamp(dac_preamp_pv, dac_preamp_rbv_pv, dac_preamp):
    """ Test dac_preamp (positive tests) """
    dac_preamp_pv.put(dac_preamp, wait=True)
    ans = dac_preamp_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_preamp}; | Value read: {ans}")
    assert ans == dac_preamp


@pytest.mark.parametrize("dac_preamp", [-1, -255, 256])
def test_dac_preamp_invalid_range(dac_preamp_pv, dac_preamp_rbv_pv,
                                  dac_preamp):
    """ Test dac_preamp (invalid tests) """
    prev_value = dac_preamp_rbv_pv.get(use_monitor=False)
    dac_preamp_pv.put(dac_preamp, wait=True)
    ans = dac_preamp_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_preamp} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_rpz", [0, 1, 255])
def test_dac_rpz(dac_rpz_pv, dac_rpz_rbv_pv, dac_rpz):
    """ Test dac_rpz (positive tests) """
    dac_rpz_pv.put(dac_rpz, wait=True)
    ans = dac_rpz_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_rpz}; | Value read: {ans}")
    assert ans == dac_rpz


@pytest.mark.parametrize("dac_rpz", [-1, -255, 256])
def test_dac_rpz_invalid_range(dac_rpz_pv, dac_rpz_rbv_pv, dac_rpz):
    """ Test dac_rpz (invalid tests) """
    prev_value = dac_rpz_rbv_pv.get(use_monitor=False)
    dac_rpz_pv.put(dac_rpz, wait=True)
    ans = dac_rpz_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_rpz} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_shaper", [0, 1, 255])
def test_dac_shaper(dac_shaper_pv, dac_shaper_rbv_pv, dac_shaper):
    """ Test dac_shaper (positive tests) """
    dac_shaper_pv.put(dac_shaper, wait=True)
    ans = dac_shaper_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_shaper}; | Value read: {ans}")
    assert ans == dac_shaper


@pytest.mark.parametrize("dac_shaper", [-1, -255, 256])
def test_dac_shaper_invalid_range(dac_shaper_pv, dac_shaper_rbv_pv,
                                  dac_shaper):
    """ Test dac_shaper (invalid tests) """
    prev_value = dac_shaper_rbv_pv.get(use_monitor=False)
    dac_shaper_pv.put(dac_shaper, wait=True)
    ans = dac_shaper_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_shaper} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_tpbufferin", [0, 1, 255])
def test_dac_tpbufferin(dac_tpbufferin_pv, dac_tpbufferin_rbv_pv,
                        dac_tpbufferin):
    """ Test dac_tpbufferin (positive tests) """
    dac_tpbufferin_pv.put(dac_tpbufferin, wait=True)
    ans = dac_tpbufferin_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tpbufferin}; | Value read: {ans}")
    assert ans == dac_tpbufferin


@pytest.mark.parametrize("dac_tpbufferin", [-1, -255, 256])
def test_dac_tpbufferin_invalid_range(dac_tpbufferin_pv, dac_tpbufferin_rbv_pv,
                                      dac_tpbufferin):
    """ Test dac_tpbufferin (invalid tests) """
    prev_value = dac_tpbufferin_rbv_pv.get(use_monitor=False)
    dac_tpbufferin_pv.put(dac_tpbufferin, wait=True)
    ans = dac_tpbufferin_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tpbufferin} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_tpbufferout", [0, 1, 255])
def test_dac_tpbufferout(dac_tpbufferout_pv, dac_tpbufferout_rbv_pv,
                         dac_tpbufferout):
    """ Test dac_tpbufferout (positive tests) """
    dac_tpbufferout_pv.put(dac_tpbufferout, wait=True)
    ans = dac_tpbufferout_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tpbufferout}; | Value read: {ans}")
    assert ans == dac_tpbufferout


@pytest.mark.parametrize("dac_tpbufferout", [-1, -255, 256])
def test_dac_tpbufferout_invalid_range(dac_tpbufferout_pv,
                                       dac_tpbufferout_rbv_pv,
                                       dac_tpbufferout):
    """ Test dac_tpbufferout (invalid tests) """
    prev_value = dac_tpbufferout_rbv_pv.get(use_monitor=False)
    dac_tpbufferout_pv.put(dac_tpbufferout, wait=True)
    ans = dac_tpbufferout_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tpbufferout} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_tpref", [0, 1, 255])
def test_dac_tpref(dac_tpref_pv, dac_tpref_rbv_pv, dac_tpref):
    """ Test dac_tpref (positive tests) """
    dac_tpref_pv.put(dac_tpref, wait=True)
    ans = dac_tpref_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tpref}; | Value read: {ans}")
    assert ans == dac_tpref


@pytest.mark.parametrize("dac_tpref", [-1, -511, 512])
def test_dac_tpref_invalid_range(dac_tpref_pv, dac_tpref_rbv_pv, dac_tpref):
    """ Test dac_tpref (invalid tests) """
    prev_value = dac_tpref_rbv_pv.get(use_monitor=False)
    dac_tpref_pv.put(dac_tpref, wait=True)
    ans = dac_tpref_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tpref} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_tprefa", [0, 1, 511])
def test_dac_tprefa(dac_tprefa_pv, dac_tprefa_rbv_pv, dac_tprefa):
    """ Test dac_tprefa (positive tests) """
    dac_tprefa_pv.put(dac_tprefa, wait=True)
    ans = dac_tprefa_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tprefa}; | Value read: {ans}")
    assert ans == dac_tprefa


@pytest.mark.parametrize("dac_tprefa", [-1, -511, 512])
def test_dac_tprefa_invalid_range(dac_tprefa_pv, dac_tprefa_rbv_pv,
                                  dac_tprefa):
    """ Test dac_tprefa (invalid tests) """
    prev_value = dac_tprefa_rbv_pv.get(use_monitor=False)
    dac_tprefa_pv.put(dac_tprefa, wait=True)
    ans = dac_tprefa_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tprefa} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_tprefb", [0, 1, 511])
def test_dac_tprefb(dac_tprefb_pv, dac_tprefb_rbv_pv, dac_tprefb):
    """ Test dac_tprefb (positive tests) """
    dac_tprefb_pv.put(dac_tprefb, wait=True)
    ans = dac_tprefb_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tprefb}; | Value read: {ans}")
    assert ans == dac_tprefb


@pytest.mark.parametrize("dac_tprefb", [-1, -511, 512])
def test_dac_tprefb_invalid_range(dac_tprefb_pv, dac_tprefb_rbv_pv,
                                  dac_tprefb):
    """ Test dac_tprefb (invalid tests) """
    prev_value = dac_tprefb_rbv_pv.get(use_monitor=False)
    dac_tprefb_pv.put(dac_tprefb, wait=True)
    ans = dac_tprefb_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_tprefb} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_thresholdenergy0", [0, 1, 511])
def test_dac_thresholdenergy0(dac_thresholdenergy0_pv,
                              dac_thresholdenergy0_rbv_pv,
                              dac_thresholdenergy0):
    """ Test dac_thresholdenergy0 (positive tests) """
    dac_thresholdenergy0_pv.put(dac_thresholdenergy0, wait=True)
    ans = dac_thresholdenergy0_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy0}; | Value read: {ans}")
    assert ans == dac_thresholdenergy0


@pytest.mark.parametrize("dac_thresholdenergy0", [-1, -511, 512])
def test_dac_thresholdenergy0_invalid_range(dac_thresholdenergy0_pv,
                                            dac_thresholdenergy0_rbv_pv,
                                            dac_thresholdenergy0):
    """ Test dac_thresholdenergy0 (invalid tests) """
    prev_value = dac_thresholdenergy0_rbv_pv.get(use_monitor=False)
    dac_thresholdenergy0_pv.put(dac_thresholdenergy0, wait=True)
    ans = dac_thresholdenergy0_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy0} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_thresholdenergy1", [0, 1, 511])
def test_dac_thresholdenergy1(dac_thresholdenergy1_pv,
                              dac_thresholdenergy1_rbv_pv,
                              dac_thresholdenergy1):
    """ Test dac_thresholdenergy1 (positive tests) """
    dac_thresholdenergy1_pv.put(dac_thresholdenergy1, wait=True)
    ans = dac_thresholdenergy1_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy1}; | Value read: {ans}")
    assert ans == dac_thresholdenergy1


@pytest.mark.parametrize("dac_thresholdenergy1", [-1, -511, 512])
def test_dac_thresholdenergy1_invalid_range(dac_thresholdenergy1_pv,
                                            dac_thresholdenergy1_rbv_pv,
                                            dac_thresholdenergy1):
    """ Test dac_thresholdenergy0 (invalid tests) """
    prev_value = dac_thresholdenergy1_rbv_pv.get(use_monitor=False)
    dac_thresholdenergy1_pv.put(dac_thresholdenergy1, wait=True)
    ans = dac_thresholdenergy1_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy1} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_thresholdenergy2", [0, 1, 511])
def test_dac_thresholdenergy2(dac_thresholdenergy2_pv,
                              dac_thresholdenergy2_rbv_pv,
                              dac_thresholdenergy2):
    """ Test dac_thresholdenergy2 (positive tests) """
    dac_thresholdenergy2_pv.put(dac_thresholdenergy2, wait=True)
    ans = dac_thresholdenergy2_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy2}; | Value read: {ans}")
    assert ans == dac_thresholdenergy2


@pytest.mark.parametrize("dac_thresholdenergy2", [-1, -511, 512])
def test_dac_thresholdenergy2_invalid_range(dac_thresholdenergy2_pv,
                                            dac_thresholdenergy2_rbv_pv,
                                            dac_thresholdenergy2):
    """ Test dac_thresholdenergy2 (invalid tests) """
    prev_value = dac_thresholdenergy2_rbv_pv.get(use_monitor=False)
    dac_thresholdenergy2_pv.put(dac_thresholdenergy2, wait=True)
    ans = dac_thresholdenergy2_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy2} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_thresholdenergy3", [0, 1, 511])
def test_dac_thresholdenergy3(dac_thresholdenergy3_pv,
                              dac_thresholdenergy3_rbv_pv,
                              dac_thresholdenergy3):
    """ Test dac_thresholdenergy3 (positive tests) """
    dac_thresholdenergy3_pv.put(dac_thresholdenergy3, wait=True)
    ans = dac_thresholdenergy3_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy3}; | Value read: {ans}")
    assert ans == dac_thresholdenergy3


@pytest.mark.parametrize("dac_thresholdenergy3", [-1, -511, 512])
def test_dac_thresholdenergy3_invalid_range(dac_thresholdenergy3_pv,
                                            dac_thresholdenergy3_rbv_pv,
                                            dac_thresholdenergy3):
    """ Test dac_thresholdenergy3 (invalid tests) """
    prev_value = dac_thresholdenergy3_rbv_pv.get(use_monitor=False)
    dac_thresholdenergy3_pv.put(dac_thresholdenergy3, wait=True)
    ans = dac_thresholdenergy3_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy3} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_thresholdenergy4", [0, 1, 511])
def test_dac_thresholdenergy4(dac_thresholdenergy4_pv,
                              dac_thresholdenergy4_rbv_pv,
                              dac_thresholdenergy4):
    """ Test dac_thresholdenergy4 (positive tests) """
    dac_thresholdenergy4_pv.put(dac_thresholdenergy4, wait=True)
    ans = dac_thresholdenergy4_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy4}; | Value read: {ans}")
    assert ans == dac_thresholdenergy4


@pytest.mark.parametrize("dac_thresholdenergy4", [-1, -511, 512])
def test_dac_thresholdenergy4_invalid_range(dac_thresholdenergy4_pv,
                                            dac_thresholdenergy4_rbv_pv,
                                            dac_thresholdenergy4):
    """ Test dac_thresholdenergy4 (invalid tests) """
    prev_value = dac_thresholdenergy4_rbv_pv.get(use_monitor=False)
    dac_thresholdenergy4_pv.put(dac_thresholdenergy4, wait=True)
    ans = dac_thresholdenergy4_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy4} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_thresholdenergy5", [0, 1, 511])
def test_dac_thresholdenergy5(dac_thresholdenergy5_pv,
                              dac_thresholdenergy5_rbv_pv,
                              dac_thresholdenergy5):
    """ Test dac_thresholdenergy5 (positive tests) """
    dac_thresholdenergy5_pv.put(dac_thresholdenergy5, wait=True)
    ans = dac_thresholdenergy5_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy5}; | Value read: {ans}")
    assert ans == dac_thresholdenergy5


@pytest.mark.parametrize("dac_thresholdenergy5", [-1, -511, 512])
def test_dac_thresholdenergy5_invalid_range(dac_thresholdenergy5_pv,
                                            dac_thresholdenergy5_rbv_pv,
                                            dac_thresholdenergy5):
    """ Test dac_thresholdenergy5 (invalid tests) """
    prev_value = dac_thresholdenergy5_rbv_pv.get(use_monitor=False)
    dac_thresholdenergy5_pv.put(dac_thresholdenergy5, wait=True)
    ans = dac_thresholdenergy5_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy5} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_thresholdenergy6", [0, 1, 511])
def test_dac_thresholdenergy6(dac_thresholdenergy6_pv,
                              dac_thresholdenergy6_rbv_pv,
                              dac_thresholdenergy6):
    """ Test dac_thresholdenergy6 (positive tests) """
    dac_thresholdenergy6_pv.put(dac_thresholdenergy6, wait=True)
    ans = dac_thresholdenergy6_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy6}; | Value read: {ans}")
    assert ans == dac_thresholdenergy6


@pytest.mark.parametrize("dac_thresholdenergy6", [-1, -511, 512])
def test_dac_thresholdenergy6_invalid_range(dac_thresholdenergy6_pv,
                                            dac_thresholdenergy6_rbv_pv,
                                            dac_thresholdenergy6):
    """ Test dac_thresholdenergy6 (invalid tests) """
    prev_value = dac_thresholdenergy6_rbv_pv.get(use_monitor=False)
    dac_thresholdenergy6_pv.put(dac_thresholdenergy6, wait=True)
    ans = dac_thresholdenergy6_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy6} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("dac_thresholdenergy7", [0, 1, 511])
def test_dac_thresholdenergy7(dac_thresholdenergy7_pv,
                              dac_thresholdenergy7_rbv_pv,
                              dac_thresholdenergy7):
    """ Test dac_thresholdenergy7 (positive tests) """
    dac_thresholdenergy7_pv.put(dac_thresholdenergy7, wait=True)
    ans = dac_thresholdenergy7_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy7}; | Value read: {ans}")
    assert ans == dac_thresholdenergy7


@pytest.mark.parametrize("dac_thresholdenergy7", [-1, -511, 512])
def test_dac_thresholdenergy7_invalid_range(dac_thresholdenergy7_pv,
                                            dac_thresholdenergy7_rbv_pv,
                                            dac_thresholdenergy7):
    """ Test dac_thresholdenergy7 (invalid tests) """
    prev_value = dac_thresholdenergy7_rbv_pv.get(use_monitor=False)
    dac_thresholdenergy7_pv.put(dac_thresholdenergy7, wait=True)
    ans = dac_thresholdenergy7_rbv_pv.get(use_monitor=False)
    print(f"Value set: {dac_thresholdenergy7} | Value read: {ans}")
    assert ans == prev_value
