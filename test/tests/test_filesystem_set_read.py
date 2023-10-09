import pytest

import numpy as np
from pathlib import Path


def uint8_to_str(data: np.ndarray):
    assert data.dtype == np.uint8
    bytes_data =  bytes(data).rstrip(b"\x00")
    return bytes_data.decode("ascii")


@pytest.mark.parametrize("autoincrement", [0, 1])
def test_autoincrement(autoincrement_pv, autoincrement_rbv_pv, autoincrement):
    """ Test acquisition to shared memory (positive tests) """
    autoincrement_pv.put(autoincrement, wait=True)
    ans = autoincrement_rbv_pv.get(use_monitor=False)
    print(f"Value set: {autoincrement}; | Value read: {ans}")
    assert ans == bool(autoincrement)


@pytest.mark.parametrize("autoincrement", [-1, 2])
def test_autoincrement_invalid_range(autoincrement_pv, autoincrement_rbv_pv,
                                     autoincrement):
    """ Test acquisition to shared memory (positive tests) """
    prev_value = autoincrement_rbv_pv.get(use_monitor=False)
    autoincrement_pv.put(autoincrement, wait=True)
    ans = autoincrement_rbv_pv.get(use_monitor=False)
    print(f"Value set: {autoincrement}; | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("autosave", [0, 1])
def test_autosave(autosave_pv, autosave_rbv_pv, autosave):
    """ Test autosave (positive tests) """
    autosave_pv.put(autosave, wait=True)
    ans = autosave_rbv_pv.get(use_monitor=False)
    print(f"Value set: {autosave}; | Value read: {ans}")
    assert ans == autosave


@pytest.mark.parametrize("autosave", [-1, -255, 256, 2])
def test_autosave_invalid_range(autosave_pv, autosave_rbv_pv, autosave):
    """ Test autosave (invalid tests) """
    prev_value = autosave_rbv_pv.get(use_monitor=False)
    autosave_pv.put(autosave, wait=True)
    ans = autosave_rbv_pv.get(use_monitor=False)
    print(f"Value set: {autosave} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("filename", ["filename.hdf5", "filename_without_extension",
                                      ("filename_way_longer" * 100) + ".hdf5"])
@pytest.mark.skip()
def test_filename(filename_pv, filename_rbv_pv, filename):
    """ Test filename (positive tests) """
    filename_pv.put(filename, wait=True)
    ans = uint8_to_str(filename_rbv_pv.get(use_monitor=False))
    print(f"Value set: {filename}; | Value read: {ans}")
    assert ans == filename

@pytest.mark.parametrize("filename", ["", "/somepath/should_not_work"])
@pytest.mark.skip()
def test_filename_invalid_range(filename_pv, filename_rbv_pv, filename):
    """ Test filename (invalid tests) """
    prev_value = uint8_to_str(filename_rbv_pv.get(use_monitor=False))
    filename_pv.put(filename, wait=True)
    ans = uint8_to_str(filename_rbv_pv.get(use_monitor=False))
    print(f"Value set: {filename} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.parametrize("filenumber", [0, 1, 255, 1024, 2**31 - 1])
def test_filenumber(filenumber_pv, filenumber_rbv_pv, filenumber):
    """ Test filenumber (positive tests) """
    filenumber_pv.put(filenumber, wait=True)
    ans = filenumber_rbv_pv.get(use_monitor=False)
    print(f"Value set: {filenumber}; | Value read: {ans}")
    assert ans == filenumber


# TODO: fix this implementation, the api is accepting any value (inclusing negative numbers)
@pytest.mark.skip()
@pytest.mark.parametrize("filenumber", [-1, -255])
def test_filenumber_invalid_range(filenumber_pv, filenumber_rbv_pv,
                                  filenumber):
    """ Test filenumber (invalid tests) """
    prev_value = filenumber_rbv_pv.get(use_monitor=False)
    filenumber_pv.put(filenumber, wait=True)
    ans = filenumber_rbv_pv.get(use_monitor=False)
    print(f"Value set: {filenumber} | Value read: {ans}")
    assert ans == prev_value


# TODO: we need to improve the input of values here.
# also, our limit for string size is quite small, only 255 characters
@pytest.mark.skip()
@pytest.mark.parametrize("filepath", ["/somepath", "/somelongerpath/" * 100])
def test_filepath(filepath_pv, filepath_rbv_pv, filepath):
    """ Test filepath (positive tests) """
    filepath_pv.put(filepath, wait=True)
    ans = uint8_to_str(filepath_rbv_pv.get(use_monitor=False))
    print(f"Value set: {filepath}; | Value read: {ans}")
    assert Path(ans) == Path(filepath)


@pytest.mark.skip()
@pytest.mark.parametrize("filepath", [
    "", "invalidpath", "\\invaliddelimiter\\"])
def test_filepath_invalid_range(filepath_pv, filepath_rbv_pv, filepath):
    """ Test filepath (invalid tests) """
    prev_value = uint8_to_str(filepath_rbv_pv.get(use_monitor=False))
    filepath_pv.put(filepath, wait=True)
    ans = uint8_to_str(filepath_rbv_pv.get(use_monitor=False))
    print(f"Value set: {filepath} | Value read: {ans}")
    assert Path(ans) == Path(prev_value)
