import matplotlib.pyplot as p
import numpy as np

# The number of bins is equal to N//2 + 1, whereas the change per bin, Δf, is equal
# to the sampling frequency fs divided by N
def freq_bins(N, fs):

    bins = []

    for k in range(N // 2 + 1):
        bins.append(k * fs / N) # k * Δf

    return bins

def time_segs(N, fs, window_length, overlap):

    step = int(window_length * (1 - overlap))

    # The number of segments is equal to the x dimension of the spectrogram;
    # this is another way to calculate it using the args of this function
    segments = (N - window_length) // step + 1

    return np.arange(segments) * step / fs

def plot(spectrogram, time_axis, freq_axis):

    p.figure(figsize=(12, 8))

    decibel = 20 * np.log10(spectrogram)
    decibel = np.clip(decibel, 60, np.max(decibel))

    p.pcolormesh(time_axis, freq_axis, decibel, shading='auto')

    p.colorbar(label="Magnitude (dB)")
    p.xlabel("Time (s)")
    p.ylabel("Frequency (Hz)")
    p.title("Spectrogram")
    p.ylim(0, 8000)

    p.show()
