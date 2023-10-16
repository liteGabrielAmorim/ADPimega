"""Test Acquisition."""

import pytest
import os
import time
import numpy as np
from ..utils import acquire, stop


pytestmark = pytest.mark.acquisition


# ----------- Set Acquire time considering acquire period -----------
@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("acquire_time", [1e-6, 100e-6, 1e-3, 100e-3, 18446744073709551615e-6])
@pytest.mark.parametrize("numb_exposures", [1, 10, 2147483647])
def test_acquire_time_period(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode,
                             numexp, numb_exposures, minimal_gap,
                             acq_period_rbv, acquire_mode_rbv, acquisition_mode):
    """ Test acquisition time set (positive tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy", None: "Not available"}
    read_out = pytest.config.readout_counter
    if acquisition_mode in (2, 3):
        read_out *= 2
    min_acq_time = 1e-6
    acquire_period = acquire_time + minimal_gap + read_out
    acq_time.put(min_acq_time, wait=True)
    acquire_mode.put(acquisition_mode, wait=True)
    numexp.put(numb_exposures, wait=True)
    acq_period.put(acquire_period, wait=True)
    acq_time.put(acquire_time, wait=True)
    ans_time = acq_time_rbv.get(use_monitor=False)
    ans_period = acq_period_rbv.get(use_monitor=False)
    acq_mode = acquire_mode_rbv.get(use_monitor=False)
    print(
        f"test_acquire_time_period acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_time == acquire_time


@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("numb_exposures", [1, 100, 2147483647])
@pytest.mark.parametrize("period_factor", [[1, 1, 0.5], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0],
                                           [0.5, 1, 0.5]])
@pytest.mark.parametrize("acquire_time", [2e-6, 100e-6, 10000000e-6, 18446744073709551e-6])
def test_acquire_time_period_neg(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode,
                                 numexp, numb_exposures, minimal_gap,
                                 period_factor, acq_period_rbv, acquire_mode_rbv,
                                 acquisition_mode):
    """ Test acquisition time set (negative tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy", None: "Not available"}
    read_out = pytest.config.readout_counter
    if acquisition_mode in (2, 3):
        read_out *= 2
    min_acq_time = 1e-6
    minimal_period = 495e-6
    acquire_period = (period_factor[0] * acquire_time + period_factor[1] * minimal_gap
                      + period_factor[2] * read_out)
    if acquire_period < minimal_period:
        acquire_period = minimal_period
    acq_time.put(min_acq_time, wait=True)
    acquire_mode.put(acquisition_mode, wait=True)
    numexp.put(numb_exposures, wait=True)
    acq_period.put(acquire_period, wait=True)
    acq_time.put(acquire_time, wait=True)
    ans_time = acq_time_rbv.get(use_monitor=False)
    ans_period = acq_period_rbv.get(use_monitor=False)
    acq_mode = acquire_mode_rbv.get(use_monitor=False)
    print(
        f"test_acquire_time_period acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_time == min_acq_time


# ----------- Set Acquire period considering acquire time -----------
@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("acquire_period", [2000e-6, 100e-3, 1844674407370955161e-6])
@pytest.mark.parametrize("numb_exposures", [1, 1000, 2147483647])
def test_acquire_period_time(acq_time, acq_period, acq_time_rbv, acquire_period, acquire_mode,
                             numexp, numb_exposures, minimal_gap,
                             acq_period_rbv, acquire_mode_rbv, acquisition_mode):
    """ Test acquisition period set (positive tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy", None: "Not available"}
    read_out = pytest.config.readout_counter
    disable_period = 0
    if acquisition_mode in (2, 3):
        read_out *= 2
    acquire_time = acquire_period - minimal_gap - read_out
    acq_period.put(disable_period, wait=True)
    acquire_mode.put(acquisition_mode, wait=True)
    numexp.put(numb_exposures, wait=True)
    acq_time.put(acquire_time, wait=True)
    acq_period.put(acquire_period, wait=True)
    ans_time = acq_time_rbv.get(use_monitor=False)
    ans_period = acq_period_rbv.get(use_monitor=False)
    acq_mode = acquire_mode_rbv.get(use_monitor=False)
    print(
        f"test_acquire_time_period acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_period == pytest.approx(acquire_period)


@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("numb_exposures", [1, 100, 2147483647])
@pytest.mark.parametrize("time_factor", [[1, 1, 0.5], [1, 0, 0.5], [1, 1, 0]])
@pytest.mark.parametrize("acquire_period", [2000e-6, 100e-3, 1844670379e-6])
def test_acquire_period_time_neg(acq_time, acq_period, acq_time_rbv, acquire_period, acquire_mode,
                                 numexp, numb_exposures, minimal_gap,
                                 time_factor, acq_period_rbv, acquire_mode_rbv,
                                 acquisition_mode):
    """ Test acquisition period set (negative tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy", None: "Not available"}
    read_out = pytest.config.readout_counter
    if acquisition_mode in (2, 3):
        read_out *= 2
    disable_period = 0
    acquire_time = (time_factor[0] * acquire_period - time_factor[1] * minimal_gap
                    - time_factor[2] * read_out)
    acq_period.put(disable_period, wait=True)
    acq_time.put(acquire_time, wait=True)
    acquire_mode.put(acquisition_mode, wait=True)
    numexp.put(numb_exposures, wait=True)
    acq_period.put(acquire_period, wait=True)
    ans_time = acq_time_rbv.get(use_monitor=False)
    ans_period = acq_period_rbv.get(use_monitor=False)
    acq_mode = acquire_mode_rbv.get(use_monitor=False)
    print(
        f"test_acquire_time_period acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_period == disable_period


# ----------- Run an acquisition -----------

@pytest.mark.parametrize("autosave", [0, 1])
@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("numb_exposures", [1, 10])
@pytest.mark.parametrize("acquire_period", [2000e-6, 100e-3, 1, 10])
def test_acquire_execution(acquisition_mode, minimal_gap, acq_time, acquire_period, acq_period,
                           acquire_mode, numb_exposures, numexp, det_acquire, capture, capture_rbv,
                           filepath_pv, autosave, autosave_pv, filename_pv, time_remaining_rbv_pv,
                           numcap, images_received_rbv_pv, images_processed_rbv_pv,
                           images_saved_rbv_pv, acq_time_rbv, acq_period_rbv, acquire_mode_rbv):
    """ Test acquisition (positive tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy", None: "Not available"}
    read_out = pytest.config.readout_counter
    offset = 2
    disable_period = 0
    success = 0
    min_acq_time = 1e-6
    expected_numb_of_frames = numb_exposures
    if acquisition_mode in (2, 3):
        read_out *= 2
    if acquisition_mode == 3:
        expected_numb_of_frames *= 2
    autosave_pv.put(autosave, wait=True)
    filepath = os.path.join(os.path.sep, "tmp")
    file_name = "test_image_" + time.strftime("%H:%M:%S", time.localtime()) + ".hdf5"
    filename_pv.put(file_name, wait=True)
    filepath_pv.put(filepath, wait=True)
    acquire_time = acquire_period - minimal_gap - read_out
    acquire_mode.put(acquisition_mode, wait=True)
    acq_time.put(min_acq_time, wait=True)
    acq_period.put(disable_period, wait=True)
    acq_time.put(acquire_time, wait=True)
    acq_period.put(acquire_period, wait=True)
    ans_time = acq_time_rbv.get(use_monitor=False)
    ans_period = acq_period_rbv.get(use_monitor=False)
    acq_mode = acquire_mode_rbv.get(use_monitor=False)
    numexp.put(numb_exposures, wait=True)
    numcap.put(numb_exposures, wait=True)
    assert acquire(det_acquire, capture, capture_rbv) == success
    expected_time_s = ans_period * numb_exposures + offset
    while expected_time_s > 0:
        expected_time_s -= 1
        if np.isclose(time_remaining_rbv_pv.get(use_monitor=False), 0):
            break
        time.sleep(1)
    max_tries = 10
    local_number_of_tries = 0
    while capture_rbv.get(as_string=True, use_monitor=False) != "Done":
        if local_number_of_tries == max_tries:
            break
        local_number_of_tries += 1
        time.sleep(1)
    time.sleep(1)
    images_received = images_received_rbv_pv.get(use_monitor=False)
    images_processed = images_processed_rbv_pv.get(use_monitor=False)
    images_saved = images_saved_rbv_pv.get(use_monitor=False)
    print(
        f" \n----------------\ntest acquire execution | acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]} | autosave: {autosave}"
        f" images received: {images_received} | images processed: {images_processed}"
        f" images saved: {images_saved} | required images: {numb_exposures}"
        f" Expected number of frmaes: {expected_numb_of_frames}")
    assert images_received == expected_numb_of_frames
    assert images_processed == expected_numb_of_frames
    if autosave:
        assert images_saved == expected_numb_of_frames
    stop(det_acquire, capture)


@pytest.mark.parametrize("stop_factor", [0, 1, 2])
@pytest.mark.parametrize("autosave", [0, 1])
@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("numb_exposures", [1, 10])
@pytest.mark.parametrize("acquire_period", [1, 10])
def test_stop_execution(acquisition_mode, minimal_gap, acq_time, acquire_period, acq_period,
                        acquire_mode, numb_exposures, numexp, det_acquire, capture, capture_rbv,
                        filepath_pv, autosave, autosave_pv, filename_pv, time_remaining_rbv_pv,
                        numcap, images_received_rbv_pv, images_processed_rbv_pv,
                        images_saved_rbv_pv, acq_time_rbv, acq_period_rbv, acquire_mode_rbv,
                        stop_factor):
    """ Test acquisition (positive tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy", None: "Not available"}
    read_out = pytest.config.readout_counter
    offset = 2
    disable_period = 0
    success = 0
    min_acq_time = 1e-6
    expected_numb_of_frames = numb_exposures
    if acquisition_mode in (2, 3):
        read_out *= 2
    if acquisition_mode == 3:
        expected_numb_of_frames *= 2
    autosave_pv.put(autosave, wait=True)
    filepath = os.path.join(os.path.sep, "tmp")
    file_name = "test_image_stop_" + time.strftime("%H:%M:%S", time.localtime()) + ".hdf5"
    filename_pv.put(file_name, wait=True)
    filepath_pv.put(filepath, wait=True)
    acquire_time = acquire_period - minimal_gap - read_out
    acquire_mode.put(acquisition_mode, wait=True)
    acq_time.put(min_acq_time, wait=True)
    acq_period.put(disable_period, wait=True)
    acq_time.put(acquire_time, wait=True)
    acq_period.put(acquire_period, wait=True)
    ans_time = acq_time_rbv.get(use_monitor=False)
    ans_period = acq_period_rbv.get(use_monitor=False)
    acq_mode = acquire_mode_rbv.get(use_monitor=False)
    numexp.put(numb_exposures, wait=True)
    numcap.put(numb_exposures, wait=True)
    assert acquire(det_acquire, capture, capture_rbv) == success
    expected_time_s = ans_period * numb_exposures + offset
    while expected_time_s > 0:
        expected_time_s -= 1
        if np.isclose(time_remaining_rbv_pv.get(use_monitor=False), 0):
            break
        if stop_factor > 0 and images_received_rbv_pv.get(use_monitor=False) > stop_factor:
            stop(det_acquire, capture)
        time.sleep(1)
    max_tries = 10
    local_number_of_tries = 0
    while capture_rbv.get(as_string=True, use_monitor=False) != "Done":
        if local_number_of_tries == max_tries:
            break
        local_number_of_tries += 1
        time.sleep(1)
    time.sleep(1)
    images_received = images_received_rbv_pv.get(use_monitor=False)
    images_processed = images_processed_rbv_pv.get(use_monitor=False)
    images_saved = images_saved_rbv_pv.get(use_monitor=False)
    print(
        f" \n----------------\ntest stop execution  | acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]} | autosave: {autosave}"
        f" images received: {images_received} | images processed: {images_processed}"
        f" images saved: {images_saved} | required images: {numb_exposures}"
        f" Expected number of frmaes: {expected_numb_of_frames} | stop factor: {stop_factor}")
    assert images_processed == images_received
    if autosave:
        assert images_saved == images_processed
    stop(det_acquire, capture)
