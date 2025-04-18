"""Test Acquisition."""

import pytest

pytestmark = pytest.mark.unit_test


# ----------- Acquire time -----------
@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("acquire_time", [1e-6, 100e-6, 1e-3, 100e-3, 18446744073709551615e-6])
def test_acquire_time(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode):
    """ Test acquisition time (positive tests) """
    disable_gap = 0
    default_mode = 0
    acquire_mode.put(default_mode, wait=True)
    acq_period.put(disable_gap, wait=True)
    acq_time.put(acquire_time, wait=True)
    ans = acq_time_rbv.get(use_monitor=False)
    print(f"Value set: {acquire_time} | Value read: {ans}")
    assert ans == acquire_time


@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("acquire_time", [0, -1])
def test_acquire_time_negative_min(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode):
    """ Test acquisition time (negative tests for lower values) """
    disable_gap = 0
    expected_value = 1e-06
    initial_value = 1
    default_mode = 0
    acquire_mode.put(default_mode, wait=True)
    acq_period.put(disable_gap, wait=True)
    acq_time.put(initial_value, wait=True)
    acq_time.put(acquire_time, wait=True)
    final_value = acq_time_rbv.get(use_monitor=False)
    print(f"Expected value: {expected_value} | Final value: {final_value}")
    assert expected_value == final_value


@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("acquire_time", [999999999999999999999999])
def test_acquire_time_negative_max(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode):
    """ Test acquisition time (negative tests for higher values) """
    expected_value = 18446744073709551615e-6
    initial_value = 1
    disable_gap = 0
    default_mode = 0
    acquire_mode.put(default_mode, wait=True)
    acq_period.put(disable_gap, wait=True)
    acq_time.put(initial_value, wait=True)
    acq_time.put(acquire_time, wait=True)
    final_value = acq_time_rbv.get(use_monitor=False)
    print(f"Expected value: {expected_value} | Final value: {final_value}")
    assert expected_value == final_value


# ----------- Acquire period -----------
@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("acquire_period", [0, 500e-6, 1e-3, 100e-3, 1844674407370955161e-6])
def test_acquire_period(acq_time, acq_period, acq_period_rbv, acquire_period, acquire_mode):
    """ Test acquisition period (positive tests) """
    remove_time_blocker = 1e-6
    default_mode = 0
    acquire_mode.put(default_mode, wait=True)
    acq_time.put(remove_time_blocker, wait=True)
    acq_period.put(acquire_period, wait=True)
    ans = acq_period_rbv.get(use_monitor=False)
    print(f"Value set: {acquire_period} | Value read: {ans}")
    assert ans == pytest.approx(acquire_period)


@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("acquire_period", [-0.01, -1])
def test_acquire_period_negative_min(acq_time, acq_period, acq_period_rbv, acquire_period,
                                     acquire_mode):
    """ Test acquisition period (negative tests for lower values) """
    initial_value = 1
    remove_time_blocker = 1e-6
    default_mode = 0
    acquire_mode.put(default_mode, wait=True)
    acq_time.put(remove_time_blocker, wait=True)
    acq_period.put(initial_value, wait=True)
    acq_period.put(acquire_period, wait=True)
    final_value = acq_period_rbv.get(use_monitor=False)
    print(f"Expected value: {initial_value} | Final value: {final_value}")
    assert initial_value == final_value


@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("acquire_period", [999999999999999999999999])
def test_acquire_period_negative_max(acq_time, acq_period, acq_period_rbv, acquire_period,
                                     acquire_mode):
    """ Test acquisition period (negative tests for higher values) """
    initial_value = 1
    remove_time_blocker = 1e-6
    default_mode = 0
    acquire_mode.put(default_mode, wait=True)
    acq_time.put(remove_time_blocker, wait=True)
    acq_period.put(initial_value, wait=True)
    acq_period.put(acquire_period, wait=True)
    final_value = acq_period_rbv.get(use_monitor=False)
    print(f"Expected value: {initial_value} | Final value: {final_value}")
    assert initial_value == final_value


# ----------- Number of exposures -----------
@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("number_exp", [1, 10, 100, 1000, 2147483647])
def test_numexp(numexp, numexp_rbv, number_exp):
    """ Test acquisition number of exposures (positive tests) """
    numexp.put(number_exp, wait=True)
    ans = numexp_rbv.get(use_monitor=False)
    print(f"Value set: {number_exp} | Value read: {ans}")
    assert ans == number_exp


@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("number_exp", [0, -1])
def test_numexp_negative_min(numexp, numexp_rbv, number_exp):
    """ Test acquisition number of exposures (negative tests for lower values) """
    initial_value = 10
    expected_value = 1
    numexp.put(initial_value, wait=True)
    numexp.put(number_exp, wait=True)
    final_value = numexp_rbv.get(use_monitor=False)
    print(f"Expected value: {expected_value} | Final value: {final_value}")
    assert expected_value == final_value


@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("number_exp", [999999999999999999999999])
def test_numexp_negative_max(numexp, numexp_rbv, number_exp):
    """ Test acquisition number of exposures (negative tests for higher values) """
    expected_value = 1
    initial_value = 10
    numexp.put(initial_value, wait=True)
    numexp.put(number_exp, wait=True)
    final_value = numexp_rbv.get(use_monitor=False)
    print(f"Expected value: {expected_value} | Final value: {final_value}")
    assert expected_value == final_value


# ----------- Number of captures (backend) -----------
@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("number_cap", [0, 1, 10, 100, 1000, 2147483647])
def test_numcap(numcap, numcap_rbv, number_cap):
    """ Test acquisition number of exposures (positive tests) """
    numcap.put(number_cap, wait=True)
    ans = numcap_rbv.get(use_monitor=False)
    print(f"Value set: {number_cap} | Value read: {ans}")
    assert ans == number_cap


@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("number_cap", [-1])
def test_numcap_negative_min(numcap, numcap_rbv, number_cap):
    """ Test acquisition number of exposures (negative tests for lower values) """
    expected_value = 0
    initial_value = 10
    numcap.put(initial_value, wait=True)
    numcap.put(number_cap, wait=True)
    final_value = numcap_rbv.get(use_monitor=False)
    print(f"Expected value: {expected_value} | Final value: {final_value}")
    assert expected_value == final_value


@pytest.mark.unit_test_acquisition
@pytest.mark.parametrize("number_cap", [999999999999999999999999])
def test_numcap_negative_max(numcap, numcap_rbv, number_cap):
    """ Test acquisition number of exposures (negative tests for higher values) """
    expected_value = 0
    initial_value = 10
    numcap.put(initial_value, wait=True)
    numcap.put(number_cap, wait=True)
    final_value = numcap_rbv.get(use_monitor=False)
    print(f"Expected value: {expected_value} | Final value: {final_value}")
    assert expected_value == final_value
