import numpy as np


def uint8_to_str(data: np.ndarray):
    if data is None:
        return ''
    assert data.dtype == np.uint8
    bytes_data =  bytes(data).rstrip(b"\x00")
    return bytes_data.decode("ascii")
