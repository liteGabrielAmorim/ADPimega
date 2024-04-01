"""
Write and Read tests for filesystem functionalities
"""

from pathlib import Path

import pytest

pytestmark = pytest.mark.unit_test
MAX_PV_CHARACTERS = 250


@pytest.mark.unit_test_filesystem
@pytest.mark.parametrize("autoincrement", [0, 1])
def test_autoincrement(autoincrement_pv, autoincrement_rbv_pv, autoincrement):
    """ Test acquisition to shared memory (positive tests) """
    autoincrement_pv.put(autoincrement, wait=True)
    ans = autoincrement_rbv_pv.get(use_monitor=False)
    print(f"Value set: {autoincrement}; | Value read: {ans}")
    assert ans == bool(autoincrement)


@pytest.mark.unit_test_filesystem
@pytest.mark.parametrize("autoincrement", [-1, 2])
def test_autoincrement_invalid_range(autoincrement_pv, autoincrement_rbv_pv,
                                     autoincrement):
    """ Test acquisition to shared memory (positive tests) """
    prev_value = autoincrement_rbv_pv.get(use_monitor=False)
    autoincrement_pv.put(autoincrement, wait=True)
    ans = autoincrement_rbv_pv.get(use_monitor=False)
    print(f"Value set: {autoincrement}; | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.unit_test_filesystem
@pytest.mark.parametrize("autosave", [0, 1])
def test_autosave(autosave_pv, autosave_rbv_pv, autosave):
    """ Test autosave (positive tests) """
    autosave_pv.put(autosave, wait=True)
    ans = autosave_rbv_pv.get(use_monitor=False)
    print(f"Value set: {autosave}; | Value read: {ans}")
    assert ans == autosave


@pytest.mark.unit_test_filesystem
@pytest.mark.parametrize("autosave", [-1, -255, 256, 2])
def test_autosave_invalid_range(autosave_pv, autosave_rbv_pv, autosave):
    """ Test autosave (invalid tests) """
    prev_value = autosave_rbv_pv.get(use_monitor=False)
    autosave_pv.put(autosave, wait=True)
    ans = autosave_rbv_pv.get(use_monitor=False)
    print(f"Value set: {autosave} | Value read: {ans}")
    assert ans == prev_value


@pytest.mark.unit_test_filesystem
@pytest.mark.parametrize("filename", ["filename.hdf5", "filename_without_extension",
                                      ("0" * MAX_PV_CHARACTERS) + ".hdf5"])
def test_filename(filename_pv, filename_rbv_pv, filename):
    """ Test filename (positive tests) """
    filename_pv.put(filename, wait=True)
    ans = filename_rbv_pv.get(use_monitor=False, as_string=True)
    print(f"Value set: {filename}; | Value read: {ans}")
    assert ans == filename


@pytest.mark.unit_test_filesystem
@pytest.mark.parametrize("filenumber", [0, 1, 255, 1024, 2**31 - 1])
def test_filenumber(filenumber_pv, filenumber_rbv_pv, filenumber):
    """ Test filenumber (positive tests) """
    filenumber_pv.put(filenumber, wait=True)
    ans = filenumber_rbv_pv.get(use_monitor=False)
    print(f"Value set: {filenumber}; | Value read: {ans}")
    assert ans == filenumber


@pytest.mark.unit_test_filesystem
@pytest.mark.parametrize("filepath", ["/somepath", "/somelongerpath/" * 15])
def test_filepath(filepath_pv, filepath_rbv_pv, filepath):
    """ Test filepath (positive tests) """
    filepath_pv.put(filepath, wait=True)
    ans = filepath_rbv_pv.get(use_monitor=False, as_string=True)
    print(f"Value set: {filepath}; | Value read: {ans}")
    assert Path(ans) == Path(filepath)
