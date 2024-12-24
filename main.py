import sys
import numpy as np
from wave import *
from dft import *
from spec import *
from plot import *

def wave(log=True):
    # Ensure the correct number of arguments have been provided
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: {sys.argv[0]} [WAVE FILE]")

    # Verify the specified file exists
    if not os.path.isfile(sys.argv[1]):
        raise FileNotFoundError(f"{sys.argv[1]} does not exist")

    # Split the header and the data
    header, data = read_wave(sys.argv[1])

    # Get sample rate and bit depth from the header
    sample_rate, bit_depth = read_header(header)

    # Decode data (signal) block
    signal = read_data(data, bit_depth)

    if log:
        print(f"Filename: {sys.argv[1]}")
        print(f"Header size: {len(header)} bytes")
        print(f"Data size: {len(data)} bytes")
        print(f"Sample rate: {sample_rate} Hz")
        print(f"Bit depth: {bit_depth} bits")
        print(f"Number of samples: {len(signal)}")

    return signal

def main():

    # Read WAVE file as a positional argument
    signal = wave()

    # These parameters control the way the spectrogram is generated
    window_size = 222
    overlap = 0.5

    # Create the spectrogram
    spectrogram = spec(signal, sample_rate, window_size, overlap)

    # These axes are necessary to plot the data correctly
    time_axis, freq_axis = axes(len(audio), sample_rate, window_size, overlap)

    # Plot the spectrogram
    plot(spectrogram, time_axis, freq_axis)

if __name__ == "__main__":
    main()
