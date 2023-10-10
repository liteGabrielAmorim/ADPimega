"""Test Acquisition."""

from test.pv import acquisition
import pytest

pytestmark = pytest.mark.acquisition


# ----------- Set Acquire time considering acquire period -----------
@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("acquire_time", [1e-6, 100e-6, 1e-3, 100e-3, 18446744073709551615e-6])
@pytest.mark.parametrize("numb_exposures", [1, 10, 2147483647])
def test_acquire_time_period(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode,
                                 numexp, numb_exposures, minimal_gap, read_out_counter,
                                 acq_period_rbv, acquire_mode_rbv, acquisition_mode):
    """ Test acquisition time set (positive tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy"}
    read_out = read_out_counter
    if acquisition_mode in (2, 3):
        read_out*=2
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
        f"test_acquire_time_period_12b acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_time == acquire_time


@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("numb_exposures", [1, 100, 2147483647])
@pytest.mark.parametrize("period_factor", [[1, 1, 0.5], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0],
                                           [0.5, 1, 0.5]])
@pytest.mark.parametrize("acquire_time", [2e-6, 100e-6, 10000000e-6, 18446744073709551e-6])
def test_acquire_time_period_neg(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode,
                                     numexp, numb_exposures, minimal_gap, read_out_counter,
                                     period_factor, acq_period_rbv, acquire_mode_rbv,
                                     acquisition_mode):
    """ Test acquisition time set (negative tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy"}
    read_out = read_out_counter
    if acquisition_mode in (2, 3):
        read_out*=2
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
        f"test_acquire_time_period_12b acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_time == min_acq_time


# ----------- Set Acquire period considering acquire time -----------
@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("acquire_period", [2000e-6, 100e-3, 18446744073709551615e-6])
@pytest.mark.parametrize("numb_exposures", [1, 1000, 2147483647])
def test_acquire_period_time(acq_time, acq_period, acq_time_rbv, acquire_period, acquire_mode,
                             numexp, numb_exposures, minimal_gap, read_out_counter,
                             acq_period_rbv, acquire_mode_rbv, acquisition_mode):
    """ Test acquisition period set (positive tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy"}
    read_out = read_out_counter
    disable_period = 0
    if acquisition_mode in (2, 3):
        read_out*=2
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
        f"test_acquire_time_period_12b acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_period == acquire_period


@pytest.mark.parametrize("acquisition_mode", [0, 1, 2, 3])
@pytest.mark.parametrize("numb_exposures", [1, 100, 2147483647])
@pytest.mark.parametrize("time_factor", [[1, 1, 0.5], [1, 0, 0.5], [1, 1, 0]])
@pytest.mark.parametrize("acquire_period", [2000e-6, 100e-3, 1844670379e-6])
def test_acquire_period_time_neg(acq_time, acq_period, acq_time_rbv, acquire_period, acquire_mode,
                                     numexp, numb_exposures, minimal_gap, read_out_counter,
                                     time_factor, acq_period_rbv, acquire_mode_rbv,
                                     acquisition_mode):
    """ Test acquisition period set (negative tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy"}
    read_out = read_out_counter
    if acquisition_mode in (2, 3):
        read_out*=2
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
        f"test_acquire_time_period_12b acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_period == disable_period


# ----------- Run an acquisition -----------


def test_acquire(acq_time, acq_period, acq_time_rbv, acquire_period, acquire_mode,
                                     numexp, numb_exposures, minimal_gap, read_out_counter,
                                     time_factor, acq_period_rbv, acquire_mode_rbv,
                                     acquisition_mode):
    """ Test acquisition time set (negative tests) """
    acq_mode_dict = {0: "Default (12 bit)", 1: "Continuous Read Write", 2: "Full Dynamic Range",
                     3: "Dual Energy"}
    read_out = read_out_counter
    if acquisition_mode in (2, 3):
        read_out*=2
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
        f"test_acquire_time_period_12b acquire time set: {acquire_time} |"
        f" acquire time read: {ans_time} | acquire period read: {ans_period} |"
        f" acquire mode: {acq_mode_dict[acq_mode]}")
    assert ans_period == disable_period




