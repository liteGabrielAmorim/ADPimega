"""
Write and Read system tests
"""

import time

import numpy as np
import pytest

from ..utils import uint8_to_str

pytestmark = pytest.mark.unit_test


@pytest.mark.unit_test_system
@pytest.mark.parametrize("allmodules", [0, 1, 2, 3])
def test_allmodules(allmodules_pv, allmodules_rbv_pv, allmodules):
    """ Test allmodules (positive tests) """
    allmodules_pv.put(allmodules, wait=True)
    ans = allmodules_rbv_pv.get(use_monitor=False)
    print(f"Value set: {allmodules}; | Value read: {ans}")
    assert ans == allmodules


@pytest.mark.unit_test_system
@pytest.mark.parametrize("allmodules", [-1, -255, 4, 5, 10, 20])
def test_allmodules_invalid_range(allmodules_pv, allmodules_rbv_pv, allmodules):
    """ Test allmodules (invalid tests) """
    initial_value = 2
    allmodules_pv.put(initial_value, wait=True)
    allmodules_pv.put(allmodules, wait=True)
    ans = allmodules_rbv_pv.get(use_monitor=False)
    print(f"Value set: {allmodules} | Value read: {ans}")
    assert ans == initial_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("extbgin", [0.0, 1.0, 0.5])
def test_extbgin(extbgin_pv, extbgin_rbv_pv, extbgin):
    """ Test extbgin (positive tests) """
    extbgin_pv.put(extbgin, wait=True)
    ans = extbgin_rbv_pv.get(use_monitor=False)
    print(f"Value set: {extbgin}; | Value read: {ans}")
    assert ans == extbgin


@pytest.mark.unit_test_system
@pytest.mark.parametrize("extbgin", [-1.0, -0.1, 1.1, 255.0, 10000.0])
def test_extbgin_invalid_range(extbgin_pv, extbgin_rbv_pv, extbgin):
    """ Test extbgin (invalid tests) """
    prev_value = extbgin_rbv_pv.get(use_monitor=False)
    extbgin_pv.put(extbgin, wait=True)
    ans = extbgin_rbv_pv.get(use_monitor=False)
    print(f"Value set: {extbgin} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("imgchipnumberid", range(1, pytest.config.chips_total + 1))
def test_imgchipnumberid(imgchipnumberid_pv, imgchipnumberid_rbv_pv, imgchipnumberid):
    """ Test imgchipnumberid (positive tests) """
    imgchipnumberid_pv.put(imgchipnumberid, wait=True)
    ans = imgchipnumberid_rbv_pv.get(use_monitor=False)
    print(f"Value set: {imgchipnumberid}; | Value read: {ans}")
    assert ans == imgchipnumberid


@pytest.mark.unit_test_system
@pytest.mark.parametrize("imgchipnumberid",
                         [pytest.config.chips_total + 1, -1, -2, -256, -255, 256])
def test_imgchipnumberid_invalid_range(imgchipnumberid_pv, imgchipnumberid_rbv_pv, imgchipnumberid):
    """ Test imgchipnumberid (invalid tests) """
    initial_value = 1
    imgchipnumberid_pv.put(initial_value, wait=True)
    imgchipnumberid_pv.put(imgchipnumberid, wait=True)
    ans = imgchipnumberid_rbv_pv.get(use_monitor=False)
    print(f"Value set: {imgchipnumberid} | Value read: {ans}")
    assert ans == initial_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("loadequalization",
                         [np.zeros((pytest.config.modules_total,), dtype="int32"),
                          np.ones((pytest.config.modules_total,), dtype="int32"),
                          np.ones((pytest.config.modules_total,), dtype="int32") * (2**31 - 1),
                          np.ones((pytest.config.modules_total,), dtype="int32") * -(2**31 - 1)])
def test_loadequalization(loadequalization_pv, loadequalization_rbv_pv, loadequalization):
    """ Test loadequalization (positive tests) """
    loadequalization_pv.put(loadequalization, wait=True)
    ans = loadequalization_rbv_pv.get(use_monitor=False)
    print(f"Value set: {loadequalization}; | Value read: {ans}")
    assert (ans == loadequalization).all()


@pytest.mark.unit_test_system
@pytest.mark.parametrize("mb_sendmode", [0, 1, 2, 3, 4])
def test_mb_sendmode(mb_sendmode_pv, mb_sendmode_rbv_pv, mb_sendmode):
    """ Test mb_sendmode (positive tests) """
    mb_sendmode_pv.put(mb_sendmode, wait=True)
    ans = mb_sendmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {mb_sendmode}; | Value read: {ans}")
    assert ans == mb_sendmode


@pytest.mark.unit_test_system
@pytest.mark.parametrize("mb_sendmode", [-1, 5, 256])
def test_mb_sendmode_invalid_range(mb_sendmode_pv, mb_sendmode_rbv_pv, mb_sendmode):
    """ Test mb_sendmode (invalid tests) """
    initial_value = 1
    mb_sendmode_pv.put(initial_value, wait=True)
    mb_sendmode_pv.put(mb_sendmode, wait=True)
    ans = mb_sendmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {mb_sendmode} | Value read: {ans}")
    assert ans == initial_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("medipixboard", range(0, pytest.config.boards_total - 1))
def test_medipixboard(medipixboard_pv, medipixboard_rbv_pv, medipixboard):
    """ Test medipixboard (positive tests) """
    medipixboard_pv.put(medipixboard, wait=True)
    ans = medipixboard_rbv_pv.get(use_monitor=False)
    print(f"Value set: {medipixboard}; | Value read: {ans}")
    assert ans == medipixboard


@pytest.mark.unit_test_system
@pytest.mark.parametrize("medipixboard", [-1, -255, -15, 15, 16, 256, pytest.config.boards_total])
def test_medipixboard_invalid_range(medipixboard_pv, medipixboard_rbv_pv, medipixboard):
    """ Test medipixboard (invalid tests) """
    initial_value = 1
    medipixboard_pv.put(initial_value, wait=True)
    medipixboard_pv.put(medipixboard, wait=True)
    ans = medipixboard_rbv_pv.get(use_monitor=False)
    print(f"Value set: {medipixboard} | Value read: {ans}")
    assert ans == initial_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("medipixmode", [0, 1, 2, 3])
def test_medipixmode(medipixmode_pv, medipixmode_rbv_pv, medipixmode):
    """ Test medipixmode (positive tests) """
    medipixmode_pv.put(medipixmode, wait=True)
    ans = medipixmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {medipixmode}; | Value read: {ans}")
    assert ans == medipixmode


@pytest.mark.unit_test_system
@pytest.mark.parametrize("medipixmode", [-1, -255, 4, 256])
def test_medipixmode_invalid_range(medipixmode_pv, medipixmode_rbv_pv, medipixmode):
    """ Test medipixmode (invalid tests) """
    initial_value = 2
    medipixmode_pv.put(initial_value, wait=True)
    medipixmode_pv.put(medipixmode, wait=True)
    ans = medipixmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {medipixmode} | Value read: {ans}")
    assert ans == initial_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("pimegamodule", range(1, pytest.config.modules_total + 1))
def test_pimegamodule(pimegamodule_pv, pimegamodule_rbv_pv, pimegamodule):
    """ Test pimegamodule (positive tests) """
    pimegamodule_pv.put(pimegamodule, wait=True)
    ans = pimegamodule_rbv_pv.get(use_monitor=False)
    print(f"Value set: {pimegamodule}; | Value read: {ans}")
    assert ans == pimegamodule


@pytest.mark.unit_test_system
@pytest.mark.parametrize("pimegamodule", [-1, 0, -255, 256])
def test_pimegamodule_invalid_range(pimegamodule_pv, pimegamodule_rbv_pv, pimegamodule):
    """ Test pimegamodule (invalid tests) """
    prev_value = pimegamodule_rbv_pv.get(use_monitor=False)
    pimegamodule_pv.put(pimegamodule, wait=True)
    ans = pimegamodule_rbv_pv.get(use_monitor=False)
    print(f"Value set: {pimegamodule} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("reset", [1, 0])
@pytest.mark.timeout(60)
def test_reset(reset_pv, iocstatusmessage_rbv_pv, reset):
    """ Test reset (positive tests) """

    reset_pv.put(reset, wait=True)
    while True:
        message = uint8_to_str(iocstatusmessage_rbv_pv.get(use_monitor=False))
        print("\n => ", message)
        if message.lower() == "reset done":
            break
        time.sleep(1)


@pytest.mark.unit_test_system
@pytest.mark.parametrize("reset_rdma_buffer", [0, 1])
def test_reset_rdma_buffer(reset_rdma_buffer_pv, reset_rdma_buffer_rbv_pv, reset_rdma_buffer):
    """ Test reset_rdma_buffer (positive tests) """
    reset_rdma_buffer_pv.put(reset_rdma_buffer, wait=True)
    ans = reset_rdma_buffer_rbv_pv.get(use_monitor=False)
    print(f"Value set: {reset_rdma_buffer}; | Value read: {ans}")
    assert ans == bool(reset_rdma_buffer)


@pytest.mark.unit_test_system
@pytest.mark.parametrize("reset_rdma_buffer", [-1, 2, -255, 256])
def test_reset_rdma_buffer_invalid_range(reset_rdma_buffer_pv,
                                         reset_rdma_buffer_rbv_pv, reset_rdma_buffer):
    """ Test reset_rdma_buffer (invalid tests) """
    prev_value = reset_rdma_buffer_rbv_pv.get(use_monitor=False)
    reset_rdma_buffer_pv.put(reset_rdma_buffer, wait=True)
    ans = reset_rdma_buffer_rbv_pv.get(use_monitor=False)
    print(f"Value set: {reset_rdma_buffer} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("select_sendimage", range(0, pytest.config.images_patterns_total))
def test_select_sendimage(select_sendimage_pv, select_sendimage_rbv_pv, select_sendimage):
    """ Test select_sendimage (positive tests) """
    select_sendimage_pv.put(select_sendimage, wait=True)
    ans = select_sendimage_rbv_pv.get(use_monitor=False)
    print(f"Value set: {select_sendimage}; | Value read: {ans}")
    assert ans == select_sendimage


@pytest.mark.unit_test_system
@pytest.mark.parametrize("select_sendimage",
                         [-1, -255, pytest.config.images_patterns_total + 1, 256])
def test_select_sendimage_invalid_range(select_sendimage_pv,
                                        select_sendimage_rbv_pv, select_sendimage):
    """ Test select_sendimage (invalid tests) """
    prev_value = select_sendimage_rbv_pv.get(use_monitor=False)
    select_sendimage_pv.put(select_sendimage, wait=True)
    ans = select_sendimage_rbv_pv.get(use_monitor=False)
    print(f"Value set: {select_sendimage} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("select_sendimage", range(0, pytest.config.images_patterns_total))
@pytest.mark.parametrize("sendimage", [0, 1, 255])
@pytest.mark.timeout(60)
def test_sendimage(select_sendimage_pv, sendimage_pv,
                   iocstatusmessage_rbv_pv, select_sendimage, sendimage):
    """ Test sendimage (positive tests) """

    select_sendimage_pv.put(select_sendimage, wait=True)
    sendimage_pv.put(sendimage, wait=True)

    while True:
        message = uint8_to_str(iocstatusmessage_rbv_pv.get(use_monitor=False))
        print("\n => ", message)
        if message.lower() == "sending image done":
            break
        time.sleep(0.1)


@pytest.mark.unit_test_system
@pytest.mark.parametrize("sendimage", [-1, 2, 255])
@pytest.mark.timeout(60)
def test_sendimage_invalid_range(sendimage_pv, iocstatusmessage_rbv_pv, sendimage):
    """ Test sendimage (positive tests) """
    sendimage_pv.put(sendimage, wait=True)

    while True:
        message = uint8_to_str(iocstatusmessage_rbv_pv.get(use_monitor=False))
        print("\n => ", message)
        if message.lower() == "sending image done":
            break
        time.sleep(0.1)


@pytest.mark.unit_test_system
@pytest.mark.parametrize("sensedacsel", range(0, pytest.config.dacs_total))
def test_sensedacsel(sensedacsel_pv, sensedacsel_rbv_pv, sensedacsel):
    """ Test sensedacsel (positive tests) """
    sensedacsel_pv.put(sensedacsel, wait=True)
    ans = sensedacsel_rbv_pv.get(use_monitor=False)
    print(f"Value set: {sensedacsel}; | Value read: {ans}")
    assert ans == sensedacsel


@pytest.mark.unit_test_system
@pytest.mark.parametrize("sensedacsel", [-1, -255, pytest.config.dacs_total + 1, 256])
def test_sensedacsel_invalid_range(sensedacsel_pv, sensedacsel_rbv_pv, sensedacsel):
    """ Test sensedacsel (invalid tests) """
    initial_value = 25
    sensedacsel_pv.put(initial_value, wait=True)
    sensedacsel_pv.put(sensedacsel, wait=True)
    ans = sensedacsel_rbv_pv.get(use_monitor=False)
    print(f"Value set: {sensedacsel} | Value read: {ans}")
    assert ans == initial_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("sensorbias", [0.5, 10.0, 15.0, 80.0, 1.0])
def test_sensorbias(sensorbias_pv, sensorbias_rbv_pv, sensorbias, medipixboard_pv):
    """ Test sensorbias (positive tests) """
    minimal_board = 0
    medipixboard_pv.put(minimal_board, wait=True)
    sensorbias_pv.put(sensorbias, wait=True)
    ans = sensorbias_rbv_pv.get(use_monitor=False)
    print(f"Value set: {sensorbias}; | Value read: {ans}")
    assert ans == pytest.approx(np.ceil(sensorbias), rel=3)


@pytest.mark.unit_test_system
@pytest.mark.parametrize("sensorbias", [-1.0, -255.0, 100.0001, 101.0, 256.0])
def test_sensorbias_invalid_range(sensorbias_pv, sensorbias_rbv_pv, sensorbias, medipixboard_pv):
    """ Test sensorbias (invalid tests) """
    minimal_board = 0
    medipixboard_pv.put(minimal_board, wait=True)
    prev_value = sensorbias_rbv_pv.get(use_monitor=False)
    sensorbias_pv.put(sensorbias, wait=True)
    ans = sensorbias_rbv_pv.get(use_monitor=False)
    print(f"Value set: {sensorbias} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("thresholdenergy", [54, 0, 1, 2, 10])
def test_thresholdenergy(thresholdenergy_pv, thresholdenergy_rbv_pv, thresholdenergy):
    """ Test thresholdenergy (positive tests) """
    thresholdenergy_pv.put(thresholdenergy, wait=True)
    ans = thresholdenergy_rbv_pv.get(use_monitor=False)
    print(f"Value set: {thresholdenergy}; | Value read: {ans}")
    assert ans == thresholdenergy


@pytest.mark.unit_test_system
@pytest.mark.parametrize("thresholdenergy", [-1, -255, 55, 256])
def test_thresholdenergy_invalid_range(thresholdenergy_pv, thresholdenergy_rbv_pv, thresholdenergy):
    """ Test thresholdenergy (invalid tests) """
    prev_value = thresholdenergy_rbv_pv.get(use_monitor=False)
    thresholdenergy_pv.put(thresholdenergy, wait=True)
    ans = thresholdenergy_rbv_pv.get(use_monitor=False)
    print(f"Value set: {thresholdenergy} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.unit_test_system
@pytest.mark.parametrize("triggermode", [0, 1, 2])
def test_triggermode(triggermode_pv, triggermode_rbv_pv, triggermode):
    """ Test triggermode (positive tests) """
    triggermode_pv.put(triggermode, wait=True)
    ans = triggermode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {triggermode}; | Value read: {ans}")
    assert ans == triggermode


@pytest.mark.unit_test_system
@pytest.mark.parametrize("triggermode", [-1, 3, 4, 15, 16, - 255, 256])
def test_triggermode_invalid_range(triggermode_pv, triggermode_rbv_pv, triggermode):
    """ Test triggermode (invalid tests) """
    initial_value = 1
    triggermode_pv.put(initial_value, wait=True)
    triggermode_pv.put(triggermode, wait=True)
    ans = triggermode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {triggermode} | Value read: {ans}")
    assert ans == initial_value
