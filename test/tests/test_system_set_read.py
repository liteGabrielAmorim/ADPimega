import pytest
import time
from ..utils import uint8_to_str
import numpy as np


@pytest.mark.parametrize("allmodules", [0, 1, 2])
def test_allmodules(allmodules_pv, allmodules_rbv_pv, allmodules):
    """ Test allmodules (positive tests) """
    allmodules_pv.put(allmodules, wait=True)
    ans = allmodules_rbv_pv.get(use_monitor=False)
    print(f"Value set: {allmodules}; | Value read: {ans}")
    assert ans == allmodules


@pytest.mark.parametrize("allmodules", [-1, -255, 4, 5])
@pytest.mark.skip()  # failing for value 4??
def test_allmodules_invalid_range(allmodules_pv, allmodules_rbv_pv, allmodules):
    """ Test allmodules (invalid tests) """
    prev_value = allmodules_rbv_pv.get(use_monitor=False)
    allmodules_pv.put(allmodules, wait=True)
    ans = allmodules_rbv_pv.get(use_monitor=False)
    print(f"Value set: {allmodules} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("extbgin", [0.0, 1.0, 0.5])
def test_extbgin(extbgin_pv, extbgin_rbv_pv, extbgin):
    """ Test extbgin (positive tests) """
    extbgin_pv.put(extbgin, wait=True)
    ans = extbgin_rbv_pv.get(use_monitor=False)
    print(f"Value set: {extbgin}; | Value read: {ans}")
    assert ans == extbgin


@pytest.mark.parametrize("extbgin", [-1.0, -0.1, 1.1, 255.0, 10000.0])
def test_extbgin_invalid_range(extbgin_pv, extbgin_rbv_pv, extbgin):
    """ Test extbgin (invalid tests) """
    prev_value = extbgin_rbv_pv.get(use_monitor=False)
    extbgin_pv.put(extbgin, wait=True)
    ans = extbgin_rbv_pv.get(use_monitor=False)
    print(f"Value set: {extbgin} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("imgchipnumberid", range(1, pytest.config.chips_total + 1))
def test_imgchipnumberid(imgchipnumberid_pv, imgchipnumberid_rbv_pv, imgchipnumberid):
    """ Test imgchipnumberid (positive tests) """
    imgchipnumberid_pv.put(imgchipnumberid, wait=True)
    ans = imgchipnumberid_rbv_pv.get(use_monitor=False)
    print(f"Value set: {imgchipnumberid}; | Value read: {ans}")
    assert ans == imgchipnumberid


@pytest.mark.parametrize("imgchipnumberid", [pytest.config.chips_total + 1, -1, -2, -256, -255, 256])
@pytest.mark.skip()  # failing for values <= -255
def test_imgchipnumberid_invalid_range(imgchipnumberid_pv, imgchipnumberid_rbv_pv, imgchipnumberid):
    """ Test imgchipnumberid (invalid tests) """
    prev_value = imgchipnumberid_rbv_pv.get(use_monitor=False)
    imgchipnumberid_pv.put(imgchipnumberid, wait=True)
    ans = imgchipnumberid_rbv_pv.get(use_monitor=False)
    print(f"Value set: {imgchipnumberid} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("loadequalization", [np.zeros((pytest.config.modules_total,), dtype='int32'),
                                              np.ones((pytest.config.modules_total,), dtype='int32'),
                                              np.ones((pytest.config.modules_total,),
                                                      dtype='int32') * (2**31-1),
                                              np.ones((pytest.config.modules_total,), dtype='int32') * -(2**31-1)])
def test_loadequalization(loadequalization_pv, loadequalization_rbv_pv, loadequalization):
    """ Test loadequalization (positive tests) """
    loadequalization_pv.put(loadequalization, wait=True)
    ans = loadequalization_rbv_pv.get(use_monitor=False)
    print(f"Value set: {loadequalization}; | Value read: {ans}")
    assert (ans == loadequalization).all()


@pytest.mark.parametrize("mb_sendmode", [0, 1, 2, 3, 4])
def test_mb_sendmode(mb_sendmode_pv, mb_sendmode_rbv_pv, mb_sendmode):
    """ Test mb_sendmode (positive tests) """
    mb_sendmode_pv.put(mb_sendmode, wait=True)
    ans = mb_sendmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {mb_sendmode}; | Value read: {ans}")
    assert ans == mb_sendmode


@pytest.mark.skip()  # TODO: failing for value 5
@pytest.mark.parametrize("mb_sendmode", [-1, 5, 256])
def test_mb_sendmode_invalid_range(mb_sendmode_pv, mb_sendmode_rbv_pv, mb_sendmode):
    """ Test mb_sendmode (invalid tests) """
    prev_value = mb_sendmode_rbv_pv.get(use_monitor=False)
    mb_sendmode_pv.put(mb_sendmode, wait=True)
    ans = mb_sendmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {mb_sendmode} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("medipixboard", range(1, pytest.config.boards_total))
def test_medipixboard(medipixboard_pv, medipixboard_rbv_pv, medipixboard):
    """ Test medipixboard (positive tests) """
    medipixboard_pv.put(medipixboard, wait=True)
    ans = medipixboard_rbv_pv.get(use_monitor=False)
    print(f"Value set: {medipixboard}; | Value read: {ans}")
    assert ans == medipixboard


@pytest.mark.skip()  # TODO: allowing values outside the range
@pytest.mark.parametrize("medipixboard", [-1, -255, 256, pytest.config.boards_total])
def test_medipixboard_invalid_range(medipixboard_pv, medipixboard_rbv_pv, medipixboard):
    """ Test medipixboard (invalid tests) """
    prev_value = medipixboard_rbv_pv.get(use_monitor=False)
    medipixboard_pv.put(medipixboard, wait=True)
    ans = medipixboard_rbv_pv.get(use_monitor=False)
    print(f"Value set: {medipixboard} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("medipixmode", [0, 1, 2, 3])
def test_medipixmode(medipixmode_pv, medipixmode_rbv_pv, medipixmode):
    """ Test medipixmode (positive tests) """
    medipixmode_pv.put(medipixmode, wait=True)
    ans = medipixmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {medipixmode}; | Value read: {ans}")
    assert ans == medipixmode


@pytest.mark.skip()  # TODO: fail to value 4
@pytest.mark.parametrize("medipixmode", [-1, -255, 4, 256])
def test_medipixmode_invalid_range(medipixmode_pv, medipixmode_rbv_pv, medipixmode):
    """ Test medipixmode (invalid tests) """
    prev_value = medipixmode_rbv_pv.get(use_monitor=False)
    medipixmode_pv.put(medipixmode, wait=True)
    ans = medipixmode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {medipixmode} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("pimegamodule", range(1, pytest.config.modules_total + 1))
def test_pimegamodule(pimegamodule_pv, pimegamodule_rbv_pv, pimegamodule):
    """ Test pimegamodule (positive tests) """
    pimegamodule_pv.put(pimegamodule, wait=True)
    ans = pimegamodule_rbv_pv.get(use_monitor=False)
    print(f"Value set: {pimegamodule}; | Value read: {ans}")
    assert ans == pimegamodule


@pytest.mark.parametrize("pimegamodule", [-1, 0, -255, 256])
def test_pimegamodule_invalid_range(pimegamodule_pv, pimegamodule_rbv_pv, pimegamodule):
    """ Test pimegamodule (invalid tests) """
    prev_value = pimegamodule_rbv_pv.get(use_monitor=False)
    pimegamodule_pv.put(pimegamodule, wait=True)
    ans = pimegamodule_rbv_pv.get(use_monitor=False)
    print(f"Value set: {pimegamodule} | Value read: {ans}")
    assert ans == prev_value


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


@pytest.mark.skip()  # TODO: implement  return error for rest invalid values
@pytest.mark.parametrize("reset", [-1, -255, 2, 255])
def test_reset_invalid_range(reset_pv, iocstatusmessage_rbv_pv, reset):
    """ Test reset (invalid tests) """
    reset_pv.put(reset, wait=True)
    message = uint8_to_str(iocstatusmessage_rbv_pv.get(use_monitor=False))
    assert message == "something"


@pytest.mark.parametrize("reset_rdma_buffer", [0, 1])
def test_reset_rdma_buffer(reset_rdma_buffer_pv, reset_rdma_buffer_rbv_pv, reset_rdma_buffer):
    """ Test reset_rdma_buffer (positive tests) """
    reset_rdma_buffer_pv.put(reset_rdma_buffer, wait=True)
    ans = reset_rdma_buffer_rbv_pv.get(use_monitor=False)
    print(f"Value set: {reset_rdma_buffer}; | Value read: {ans}")
    assert ans == bool(reset_rdma_buffer)


@pytest.mark.parametrize("reset_rdma_buffer", [-1, 2, -255, 256])
def test_reset_rdma_buffer_invalid_range(reset_rdma_buffer_pv, reset_rdma_buffer_rbv_pv, reset_rdma_buffer):
    """ Test reset_rdma_buffer (invalid tests) """
    prev_value = reset_rdma_buffer_rbv_pv.get(use_monitor=False)
    reset_rdma_buffer_pv.put(reset_rdma_buffer, wait=True)
    ans = reset_rdma_buffer_rbv_pv.get(use_monitor=False)
    print(f"Value set: {reset_rdma_buffer} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("select_sendimage", range(0, pytest.config.images_patterns_total))
def test_select_sendimage(select_sendimage_pv, select_sendimage_rbv_pv, select_sendimage):
    """ Test select_sendimage (positive tests) """
    select_sendimage_pv.put(select_sendimage, wait=True)
    ans = select_sendimage_rbv_pv.get(use_monitor=False)
    print(f"Value set: {select_sendimage}; | Value read: {ans}")
    assert ans == select_sendimage


@pytest.mark.parametrize("select_sendimage", [-1, -255, pytest.config.images_patterns_total + 1, 256])
def test_select_sendimage_invalid_range(select_sendimage_pv, select_sendimage_rbv_pv, select_sendimage):
    """ Test select_sendimage (invalid tests) """
    prev_value = select_sendimage_rbv_pv.get(use_monitor=False)
    select_sendimage_pv.put(select_sendimage, wait=True)
    ans = select_sendimage_rbv_pv.get(use_monitor=False)
    print(f"Value set: {select_sendimage} | Value read: {ans}")
    assert ans == prev_value


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


@pytest.mark.skip()  # TODO: which values are valid???
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


@pytest.mark.parametrize("sensedacsel", range(0, pytest.config.dacs_total))
def test_sensedacsel(sensedacsel_pv, sensedacsel_rbv_pv, sensedacsel):
    """ Test sensedacsel (positive tests) """
    sensedacsel_pv.put(sensedacsel, wait=True)
    ans = sensedacsel_rbv_pv.get(use_monitor=False)
    print(f"Value set: {sensedacsel}; | Value read: {ans}")
    assert ans == sensedacsel


@pytest.mark.parametrize("sensedacsel", [-1, -255, pytest.config.dacs_total + 1, 256])
@pytest.mark.skip()  # it is allowing negative values
def test_sensedacsel_invalid_range(sensedacsel_pv, sensedacsel_rbv_pv, sensedacsel):
    """ Test sensedacsel (invalid tests) """
    prev_value = sensedacsel_rbv_pv.get(use_monitor=False)
    sensedacsel_pv.put(sensedacsel, wait=True)
    ans = sensedacsel_rbv_pv.get(use_monitor=False)
    print(f"Value set: {sensedacsel} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.skip()  # when I set value one it stores the value 2???
@pytest.mark.parametrize("sensorbias", [0.0, 1.0, 1.5, 2.0, 100.0])
def test_sensorbias(sensorbias_pv, sensorbias_rbv_pv, sensorbias):
    """ Test sensorbias (positive tests) """
    sensorbias_pv.put(sensorbias, wait=True)
    ans = sensorbias_rbv_pv.get(use_monitor=False)
    print(f"Value set: {sensorbias}; | Value read: {ans}")
    assert ans == np.ceil(sensorbias)


@pytest.mark.parametrize("sensorbias", [-1.0, -255.0, 100.0001, 101.0, 256.0])
def test_sensorbias_invalid_range(sensorbias_pv, sensorbias_rbv_pv, sensorbias):
    """ Test sensorbias (invalid tests) """
    prev_value = sensorbias_rbv_pv.get(use_monitor=False)
    sensorbias_pv.put(sensorbias, wait=True)
    ans = sensorbias_rbv_pv.get(use_monitor=False)
    print(f"Value set: {sensorbias} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("thresholdenergy", [54, 0, 1, 2, 10])
def test_thresholdenergy(thresholdenergy_pv, thresholdenergy_rbv_pv, thresholdenergy):
    """ Test thresholdenergy (positive tests) """
    thresholdenergy_pv.put(thresholdenergy, wait=True)
    ans = thresholdenergy_rbv_pv.get(use_monitor=False)
    print(f"Value set: {thresholdenergy}; | Value read: {ans}")
    assert ans == thresholdenergy


@pytest.mark.parametrize("thresholdenergy", [-1, -255, 55, 256])
def test_thresholdenergy_invalid_range(thresholdenergy_pv, thresholdenergy_rbv_pv, thresholdenergy):
    """ Test thresholdenergy (invalid tests) """
    prev_value = thresholdenergy_rbv_pv.get(use_monitor=False)
    thresholdenergy_pv.put(thresholdenergy, wait=True)
    ans = thresholdenergy_rbv_pv.get(use_monitor=False)
    print(f"Value set: {thresholdenergy} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("triggermode", [0, 1, 2])
def test_triggermode(triggermode_pv, triggermode_rbv_pv, triggermode):
    """ Test triggermode (positive tests) """
    triggermode_pv.put(triggermode, wait=True)
    ans = triggermode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {triggermode}; | Value read: {ans}")
    assert ans == triggermode


@pytest.mark.skip()  # the value 3 sets 0??
@pytest.mark.parametrize("triggermode", [-1, 3, -255, 256])
def test_triggermode_invalid_range(triggermode_pv, triggermode_rbv_pv, triggermode):
    """ Test triggermode (invalid tests) """
    prev_value = triggermode_rbv_pv.get(use_monitor=False)
    triggermode_pv.put(triggermode, wait=True)
    ans = triggermode_rbv_pv.get(use_monitor=False)
    print(f"Value set: {triggermode} | Value read: {ans}")
    assert ans == prev_value
