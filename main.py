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
    parser.add_argument("-w", "--window-length",
                        type = int,
                        choices = range(2, 1000),
                        default = 20,
                        metavar = "INTEGER",
                        help = "window length in milliseconds")
    parser.add_argument("-f", "--window-function",
                        choices = ["hanning", "hamming", "blackman"],
                        default = "hanning",
                        help = "window function")
    parser.add_argument("-o", "--overlap",
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

    window_functions = {
        "hanning": np.hanning,
        "hamming": np.hamming,
        "blackman": np.blackman,
    }

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
    window_length = int(args.window_length * sample_rate / 1000)
    overlap = args.overlap

    # Create the spectrogram
    spectrogram = spec(signal, window_length, overlap, window_functions[args.window_function])

    # These axes are necessary to plot the data correctly
    time_axis, freq_axis = axes(len(signal), sample_rate, window_length, overlap)

    # Plot the spectrogram
    plot(spectrogram, time_axis, freq_axis)

if __name__ == "__main__":
    main()
