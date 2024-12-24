#!/usr/bin/python3

import sys, os
import argparse
import numpy as np
from wave import *
from dft import *
from spec import *
from plot import *
from tests import *

def main():

    # Parse arguments
    parser = argparse.ArgumentParser(
            prog = "simple-spectrogram",
            description = """a simple program that implements
            the spectrogram of a given single channel WAVE file""",
            )

    parser.add_argument("filename")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-t", "--tests", action="store_true")

    args = parser.parse_args()

    # Check if file exists; exit if not found or not file
    if not os.path.isfile(args.filename):
        raise FileNotFoundError(f"{sys.argv[1]} does not exist")

    # Split the header and the data
    header, data = read_wave(args.filename)

    # Get sample rate and bit depth from the header
    sample_rate, bit_depth = read_header(header)

    # Decode data (signal) block
    signal = read_data(data, bit_depth)

    # Print if verbose
    if args.verbose:
        print(f"Filename: {sys.argv[1]}")
        print(f"Header size: {len(header)} bytes")
        print(f"Data size: {len(data)} bytes")
        print(f"Sample rate: {sample_rate} Hz")
        print(f"Bit depth: {bit_depth} bits")
        print(f"Number of samples: {len(signal)}")

    # Run tests and exit
    if args.tests:
        test_processing_time(signal)
        exit(0)

    # These parameters control the way the spectrogram is generated
    window_size = 882
    overlap = 0.5

    # Create the spectrogram
    spectrogram = spec(signal, sample_rate, window_size, overlap)

    # These axes are necessary to plot the data correctly
    time_axis, freq_axis = axes(len(signal), sample_rate, window_size, overlap)

    # Plot the spectrogram
    plot(spectrogram, time_axis, freq_axis)

if __name__ == "__main__":
    main()
