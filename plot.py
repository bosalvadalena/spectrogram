import matplotlib.pyplot as p
import numpy as np

# This is a helper function to return the necessary axes for plotting
def axes(signal_length, sampling_rate, window_size, overlap):

    step_size = int(window_size * (1 - overlap))
    N = (signal_length - window_size) // step_size + 1
    
    freq_axis = np.fft.rfftfreq(window_size, d=1/sampling_rate)
    
    time_axis = np.arange(N) * step_size / sampling_rate
    
    return time_axis, freq_axis

# Plot the spectrogram
def plot(spectrogram, time_axis, freq_axis):

    p.figure(figsize=(10, 6))

    decibel = 20 * np.log10(spectrogram)
    decibel = np.clip(decibel, 60, np.max(decibel))

    p.pcolormesh(time_axis, freq_axis, decibel, shading='auto')

    p.colorbar(label="Magnitude (dB)")
    p.xlabel("Time (s)")
    p.ylabel("Frequency (Hz)")
    p.title("Spectrogram")
    p.ylim(0, 8000)

    p.show()
