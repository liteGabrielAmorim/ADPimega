"""
Utilities for automated tests
"""

import time

import numpy as np


def uint8_to_str(data: np.ndarray):
    """ Convert uint8 to string """
    if data is None:
        return ""
    assert data.dtype == np.uint8
    bytes_data = bytes(data).rstrip(b"\x00")
    return bytes_data.decode("ascii")


def get_detector_read_out_by_counter(config):
    """ Get the detector read out for one counter"""
    basic_read_out = 492e-6
    if config.getini("detector_model") in ("135D", "135DL", "540D"):
        return basic_read_out
    else:
        return basic_read_out * 2


def number_of_boards(config):
    """ Get the number of medipix boards """
    if config.getini("detector_model") in ("135D", "540D"):
        return 3
    else:
        return 1


def number_of_chips(config):
    """ Get the number og chips"""
    if config.getini("detector_model") in ("135D", "540D"):
        return 36
    else:
        return 12


def number_of_dacs():
    """ Return the number of DACs of the chip """
    return 32


def number_of_modules(config):
    """ Return the number of modules of the detector """
    model = config.getini("detector_model")

    if model in ("135D", "135DL"):
        return 1
    elif model == "540D":
        return 4
    else:
        return 10


def number_of_image_patterns():
    """ Return the number of image patterns """
    return 15


# ----------- Specific commands -----------
def acquire(det_acquire, capture, capture_rbv):
    """ acquire command """
    start_acq = 1
    counter = 0
    success = 0
    fail = 1
    timeout_s = 5
    capture.put(start_acq, wait=True)
    while capture_rbv.get(as_string=True, use_monitor=False) != "Capturing":
        counter += 1
        if counter > timeout_s:
            return fail
        time.sleep(1)
    det_acquire.put(start_acq, wait=True)
    return success


def stop(det_acquire, capture):
    """ acquire command """
    stop_acq = 0
    capture.put(stop_acq, wait=True)
    det_acquire.put(stop_acq, wait=True)
