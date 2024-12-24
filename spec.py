import numpy as np

# This is our windowing spectrogram function
def spec(signal, sampling_rate, window_size, overlap, window_function=np.hamming):

    step = int(window_size * (1 - overlap))

    window = window_function(window_size)
    N = (len(signal) - window_size) // step + 1

    transforms = []
    
    for i in range(N):
        begin = i * step
        end = begin + window_size
        
        segment = signal[begin:end] * window
        
        transforms.append(np.abs(np.fft.rfft(segment)))
    
    return np.array(transforms).T
