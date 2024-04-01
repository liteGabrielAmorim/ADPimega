"""
Basic PVs for filesystem tests
"""
import pytest


@pytest.fixture()
def autoincrement_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["AutoIncrement"]


@pytest.fixture()
def autoincrement_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["AutoIncrement_RBV"]


@pytest.fixture()
def autosave_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["AutoSave"]


@pytest.fixture()
def autosave_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["AutoSave_RBV"]


@pytest.fixture()
def filename_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["FileName"]


@pytest.fixture()
def filename_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["FileName_RBV"]


@pytest.fixture()
def filenumber_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["FileNumber"]


@pytest.fixture()
def filenumber_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["FileNumber_RBV"]


@pytest.fixture()
def filepath_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["FilePath"]


@pytest.fixture()
def filepath_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["FilePath_RBV"]


@pytest.fixture()
def filetemplate_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["FileTemplate_RBV"]


@pytest.fixture()
def fullfilename_rbv_pv(init_pv, dev_id):
    return init_pv[dev_id]["filesystem"]["FullFileName_RBV"]
