import pytest
import numpy as np

from epics import PV

pytestmark = pytest.mark.acquisition

ACQ_PV = {"AcquireTime": None, "AcquireTime_RBV": None}


class Acq():
    def __init__(self, epics_prefix: str, epics_camera: str) -> None:
        self.epics_prefix = epics_prefix
        self.epics_camera = epics_camera

        self.define_PVs()

    def define_PVs(self):
        #         for pv in list(ACQ_PV.keys()):
        #             Pv = PV(self.epics_prefix + self.epics_camera + suffix)
        #             setattr(self, suffix.replace(":", "_"), Pv)

        # @pytest.mark.parametrize("acquire_time", [1e-6, 100e-6, 1e-3, 100e-3, 18446744073709551615e-6])
        # def test_numexposures(pimega, acquire_time):
        #     # Set acquire time
        #     Acquisition.acq_time.put(acquire_time)
        #     # Read acquire time
        #     ans = np.round(Acquisition.acq_time.get("AcquireTime_RBV"), 3)
        #     print(f"Value set: {acquire_time} | Value read: {ans}")
        #     assert ans == acquire_time
