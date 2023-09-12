import pytest

pytestmark = pytest.mark.acquisition


@pytest.mark.parametrize("acquire_time", [1e-6, 100e-6, 1e-3, 100e-3, 18446744073709551615e-6])
def test_acquire_time(acq_time, acq_time_rbv, acquire_time):
    acq_time.put(acquire_time, wait=True)
    ans = acq_time_rbv.get()
    print(f"Value set: {acquire_time} | Value read: {ans}")
    assert ans == acquire_time


@pytest.mark.parametrize("acquire_time", [0, -1])
def test_acquire_time_negative_min(acq_time, acq_time_rbv, acquire_time):
    expected_value = 1e-06
    initial_value = 1
    acq_time.put(initial_value, wait=True)
    acq_time.put(acquire_time, wait=True)
    final_value = acq_time_rbv.get()
    print(f"Expected value: {expected_value} | Final value: {final_value}")
    assert expected_value == final_value


@pytest.mark.parametrize("acquire_time", [999999999999999999999999])
def test_acquire_time_negative_max(acq_time, acq_time_rbv, acquire_time):
    expected_value = 18446744073709551615e-6
    initial_value = 1
    acq_time.put(initial_value, wait=True)
    acq_time.put(acquire_time, wait=True)
    final_value = acq_time_rbv.get()
    print(f"Expected value: {expected_value} | Final value: {final_value}")
    assert expected_value == final_value
