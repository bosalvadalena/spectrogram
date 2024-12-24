import cmath
import numpy as np

def dft(signal):
    """
    Discrete Fourier Transform (DFT)
    """
    N = len(signal)
    transform = np.zeros(N, dtype=complex)

    for k in range(N):
        total = 0
        for n in range(N):
            total += signal[n] * cmath.exp(-2j * cmath.pi * k * n / N)
        transform[k] = total

    return transform
