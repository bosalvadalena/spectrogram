#!/usr/bin/python3

import sys
import os
import struct
import numpy as np

def read_wave(filename):
    """
    Reads a WAVE file and returns its header and data.

    The header is assumed to be 44 bytes long as per the WAVE file specification.
    Raises a ValueError if the file is not a valid WAVE file.
    """
    with open(filename, "rb") as f:
        data = f.read()

    # Verify the file is a valid WAVE file
    if data[8:12].decode("ascii") != "WAVE":
        raise ValueError(f"{filename} is not a WAVE file")

    return data[:44], data[44:]

def read_header(header):
    """
    Parses the WAVE header to extract the sample rate and bit depth.

    Args:
        header (bytes): The 44-byte WAVE file header.

    Returns:
        tuple: A tuple containing the sample rate (int) and bit depth (int).
    """
    sample_rate = struct.unpack("<I", header[24:28])[0]
    bit_depth = struct.unpack("<H", header[34:36])[0]

    return sample_rate, bit_depth

def read_data(data, bit_depth):
    """
    Converts raw audio data to a numpy array based on the bit depth.

    Args:
        data (bytes): The audio data extracted from the WAVE file.
        bit_depth (int): The bit depth of the audio (e.g., 16 for 16-bit audio).

    Returns:
        np.ndarray: The audio data as a numpy array.
    """
    # Map the bit depth to the corresponding numpy data type
    dtype = getattr(np, f'int{bit_depth}')
    return np.frombuffer(data, dtype)

def main():
    """
    Main function to process the WAVE file specified in the command-line arguments.

    Reads the WAVE file, extracts and prints the header information,
    and loads the audio data into a numpy array.
    """
    # Ensure the correct number of arguments have been provided
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: {sys.argv[0]} [WAVE FILE]")

    # Verify the specified file exists
    if not os.path.isfile(sys.argv[1]):
        raise FileNotFoundError(f"{sys.argv[1]} does not exist")

    # Read the WAVE file and parse its header and data
    header, data = read_wave(sys.argv[1])
    print(f"Header size: {len(header)} bytes")
    print(f"Data size: {len(data)} bytes")

    sample_rate, bit_depth = read_header(header)
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Bit depth: {bit_depth} bits")

    audio = read_data(data, bit_depth)
    print(f"Number of samples: {len(audio)}")
    print(audio)

if __name__ == "__main__":
    main()
