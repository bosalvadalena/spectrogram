#!/usr/bin/python3

import struct
import numpy as np

"""
    For the WAVE header specification, see
    https://en.wikipedia.org/wiki/WAV#WAV_file_header
"""

# This function reads a WAVE file into a buffer and returns the header/data
def read_wave(filename):

    with open(filename, "rb") as f:
        data = f.read()

    # Verify the file is a valid WAVE file
    if data[8:12].decode("ascii") != "WAVE":
        raise ValueError(f"{filename} is not a WAVE file")

    return data[:44], data[44:]

# This function reads from the WAVE header and extracts two pieces of
# information that we need to process it
def read_header(header):

    sample_rate = struct.unpack("<I", header[24:28])[0]
    bit_depth = struct.unpack("<H", header[34:36])[0]

    return sample_rate, bit_depth

# This function reads the data (signal) and converts it into a Numpy array
def read_data(data, bit_depth):

    dtype = getattr(np, f'int{bit_depth}')
    return np.frombuffer(data, dtype)
