import numpy as np

def stft(signal, window_size, overlap, window_function):

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
