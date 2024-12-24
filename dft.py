import cmath
import numpy as np

# Discrete Fourier Transform (DFT)
def dft(signal):

    N = len(signal)
    transform = np.zeros(N, dtype=complex)

    for k in range(N):
        total = 0
        for n in range(N):
            total += signal[n] * cmath.exp(-2j * cmath.pi * k * n / N)
        transform[k] = total

    return transform
