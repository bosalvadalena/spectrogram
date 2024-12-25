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
            description = """a simple program that implements
            the spectrogram of a given single channel WAVE file""",
            )

    parser.add_argument("filename")
    parser.add_argument("--window",
                        type = int,
                        choices = range(2, 1000),
                        default = 20,
                        metavar = "INTEGER",
                        help = "window size in milliseconds")
    parser.add_argument("--overlap",
                        type = float,
                        choices = [i / 100 for i in range(100)],
                        default = 0.5,
                        metavar = "FLOAT",
                        help = "window overlap percent as a decimal")
    parser.add_argument("-t", "--tests", 
                        action = "store_true",
                        help = "run tests")
    parser.add_argument("-v", "--verbose",
                        action = "store_true",
                        help = "show more output")

    args = parser.parse_args()

    # Check if file exists; exit if not found or not file
    if not os.path.isfile(args.filename):
        raise FileNotFoundError(f"{args.filename} does not exist")

    # Split the header and the data
    header, data = read_wave(args.filename)

    # Get sample rate and bit depth from the header
    sample_rate, bit_depth = read_header(header)

    # Decode data (signal) block
    signal = read_data(data, bit_depth)

    # Print if verbose
    if args.verbose:
        print(f"Filename: {args.filename}")
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
    window_size = int(args.window * sample_rate / 1000)
    overlap = args.overlap

    # Create the spectrogram
    spectrogram = spec(signal, sample_rate, window_size, overlap)

    # These axes are necessary to plot the data correctly
    time_axis, freq_axis = axes(len(signal), sample_rate, window_size, overlap)

    # Plot the spectrogram
    plot(spectrogram, time_axis, freq_axis)

if __name__ == "__main__":
    main()
