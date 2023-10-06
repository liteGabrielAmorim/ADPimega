"""Test Acquisition."""

from test.pv import acquisition
import pytest

pytestmark = pytest.mark.acquisition


# ----------- Set Acquire time considering acquire period -----------
@pytest.mark.parametrize("acquire_time", [1e-6, 100e-6, 1e-3, 100e-3, 18446744073709551615e-6])
@pytest.mark.parametrize("numb_exposures", [1, 10, 1000, 2147483647])
def test_acquire_time_period_12b(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode,
                                 numexp, numb_exposures, minimal_gap, read_out_counter):
    """ Test acquisition time for 12 bit mode (positive tests) """
    acquisition_mode = 0
    numb_exposures = 2
    min_acq_time = 1e-6
    acquire_period = acquire_time + minimal_gap + read_out_counter
    acq_time.put(min_acq_time, wait=True)
    acquire_mode.put(acquisition_mode, wait=True)
    numexp.put(numb_exposures, wait=True)
    acq_period.put(acquire_period, wait=True)
    acq_time.put(acquire_time, wait=True)
    ans = acq_time_rbv.get(use_monitor=False)
    print(
        "test_acquire_time_period_12b "
        f"acquire time set: {acquire_time} | acquire time read: {ans} | "
        f"acquire period read: {acquire_period}")
    assert ans == acquire_time

# TODO (Robert). Conclude this negative test
# @pytest.mark.parametrize("acquire_time", [1e-6, 100e-6, 18446744073709551615e-6])
# @pytest.mark.parametrize("numb_exposures", [1, 100, 2147483647])
# @pytest.mark.parametrize("period_factor", [[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0],
#                                            [0.5, 1, 0.5], [1, 0.5, 1], [1, 1, 0.5]])
# def test_acquire_time_period_12b_neg(acq_time, acq_period, acq_time_rbv, acquire_time, acquire_mode,
#                                      numexp, numb_exposures, minimal_gap, read_out_counter,
#                                      period_factor):
#     """ Test acquisition time for 12 bit mode (negative tests) """
#     acquisition_mode = 0
#     numb_exposures = 2
#     min_acq_time = 1e-6
#     acquire_period = (period_factor[0] * acquire_time + period_factor[1] * minimal_gap
#                       + period_factor[2] * read_out_counter)
#     acq_time.put(min_acq_time, wait=True)
#     acquire_mode.put(acquisition_mode, wait=True)
#     numexp.put(numb_exposures, wait=True)
#     acq_period.put(acquire_period, wait=True)
#     acq_time.put(acquire_time, wait=True)
#     ans = acq_time_rbv.get(use_monitor=False)
#     print(
#         "test_acquire_time_period_12b_neg "
#         f"acquire time set: {acquire_time} | acquire time read: {ans} | "
#         f"acquire period read: {acquire_period}")
#     assert ans == acquire_time


# @pytest.mark.parametrize("acquire_time", [0, -1])
# def test_acquire_time_negative_min(acq_time, acq_period, acq_time_rbv, acquire_time):
#     """ Test acquisition time (negative tests for lower values) """
#     disable_gap = 0
#     expected_value = 1e-06
#     initial_value = 1
#     acq_period.put(disable_gap, wait=True)
#     acq_time.put(initial_value, wait=True)
#     acq_time.put(acquire_time, wait=True)
#     final_value = acq_time_rbv.get(use_monitor=False)
#     print(f"Expected value: {expected_value} | Final value: {final_value}")
#     assert expected_value == final_value


# @pytest.mark.parametrize("acquire_time", [999999999999999999999999])
# def test_acquire_time_negative_max(acq_time, acq_period, acq_time_rbv, acquire_time):
#     """ Test acquisition time (negative tests for higher values) """
#     expected_value = 18446744073709551615e-6
#     initial_value = 1
#     disable_gap = 0
#     acq_period.put(disable_gap, wait=True)
#     acq_time.put(initial_value, wait=True)
#     acq_time.put(acquire_time, wait=True)
#     final_value = acq_time_rbv.get(use_monitor=False)
#     print(f"Expected value: {expected_value} | Final value: {final_value}")
#     assert expected_value == final_value


# # ----------- Acquire period -----------
# @pytest.mark.parametrize("acquire_period", [0, 500e-6, 1e-3, 100e-3, 18446744073709551615e-6])
# def test_acquire_period(acq_time, acq_period, acq_period_rbv, acquire_period):
#     """ Test acquisition period (positive tests) """
#     remove_time_blocker = 1e-6
#     acq_time.put(remove_time_blocker, wait=True)
#     acq_period.put(acquire_period, wait=True)
#     ans = acq_period_rbv.get(use_monitor=False)
#     print(f"Value set: {acquire_period} | Value read: {ans}")
#     assert ans == acquire_period


# # TODO: fix the error on IOC (disable during test implementation)
# # Acquire period is accepting any value
# @pytest.mark.skip()
# @pytest.mark.parametrize("acquire_period", [-0.01, -1])
# def test_acquire_period_negative_min(acq_time, acq_period, acq_period_rbv, acquire_period):
#     """ Test acquisition period (negative tests for lower values) """
#     expected_value = 1e-06
#     initial_value = 1
#     remove_time_blocker = 1e-6
#     acq_time.put(remove_time_blocker, wait=True)
#     acq_period.put(initial_value, wait=True)
#     acq_period.put(acquire_period, wait=True)
#     final_value = acq_period_rbv.get(use_monitor=False)
#     print(f"Expected value: {expected_value} | Final value: {final_value}")
#     assert expected_value == final_value


# # TODO: fix the error on IOC (disable during test implementation)
# # WARNING: fix the error on ioc
# @pytest.mark.skip()
# @pytest.mark.parametrize("acquire_period", [999999999999999999999999])
# def test_acquire_period_negative_max(acq_time, acq_period, acq_period_rbv, acquire_period):
#     """ Test acquisition period (negative tests for higher values) """
#     expected_value = 18446744073709551615e-6
#     initial_value = 1
#     remove_time_blocker = 1e-6
#     acq_time.put(remove_time_blocker, wait=True)
#     acq_period.put(initial_value, wait=True)
#     acq_period.put(acquire_period, wait=True)
#     final_value = acq_period_rbv.get(use_monitor=False)
#     print(f"Expected value: {expected_value} | Final value: {final_value}")
#     assert expected_value == final_value


# # ----------- Number of exposures -----------
# @pytest.mark.parametrize("number_exp", [1, 10, 100, 1000, 2147483647])
# def test_numexp(numexp, numexp_rbv, number_exp):
#     """ Test acquisition number of exposures (positive tests) """
#     numexp.put(number_exp, wait=True)
#     ans = numexp_rbv.get(use_monitor=False)
#     print(f"Value set: {number_exp} | Value read: {ans}")
#     assert ans == number_exp


# @pytest.mark.parametrize("number_exp", [0, -1])
# def test_numexp_negative_min(numexp, numexp_rbv, number_exp):
#     """ Test acquisition number of exposures (negative tests for lower values) """
#     initial_value = 10
#     expected_value = 1
#     numexp.put(initial_value, wait=True)
#     numexp.put(number_exp, wait=True)
#     final_value = numexp_rbv.get(use_monitor=False)
#     print(f"Expected value: {expected_value} | Final value: {final_value}")
#     assert expected_value == final_value


# @pytest.mark.parametrize("number_exp", [999999999999999999999999])
# def test_numexp_negative_max(numexp, numexp_rbv, number_exp):
#     """ Test acquisition number of exposures (negative tests for higher values) """
#     expected_value = 1
#     initial_value = 10
#     numexp.put(initial_value, wait=True)
#     numexp.put(number_exp, wait=True)
#     final_value = numexp_rbv.get(use_monitor=False)
#     print(f"Expected value: {expected_value} | Final value: {final_value}")
#     assert expected_value == final_value


# # ----------- Number of captures (backend) -----------
# @pytest.mark.parametrize("number_cap", [0, 1, 10, 100, 1000, 2147483647])
# def test_numcap(numcap, numcap_rbv, number_cap):
#     """ Test acquisition number of exposures (positive tests) """
#     numcap.put(number_cap, wait=True)
#     ans = numcap_rbv.get(use_monitor=False)
#     print(f"Value set: {number_cap} | Value read: {ans}")
#     assert ans == number_cap


# @pytest.mark.parametrize("number_cap", [-1])
# def test_numcap_negative_min(numcap, numcap_rbv, number_cap):
#     """ Test acquisition number of exposures (negative tests for lower values) """
#     expected_value = 0
#     initial_value = 10
#     numcap.put(initial_value, wait=True)
#     numcap.put(number_cap, wait=True)
#     final_value = numcap_rbv.get(use_monitor=False)
#     print(f"Expected value: {expected_value} | Final value: {final_value}")
#     assert expected_value == final_value


# @pytest.mark.parametrize("number_cap", [999999999999999999999999])
# def test_numcap_negative_max(numcap, numcap_rbv, number_cap):
#     """ Test acquisition number of exposures (negative tests for higher values) """
#     expected_value = 0
#     initial_value = 10
#     numcap.put(initial_value, wait=True)
#     numcap.put(number_cap, wait=True)
#     final_value = numcap_rbv.get(use_monitor=False)
#     print(f"Expected value: {expected_value} | Final value: {final_value}")
#     assert expected_value == final_value
