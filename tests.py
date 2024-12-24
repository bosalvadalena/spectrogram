import time
import numpy as np
from dft import dft

def test_processing_time(signal):

    print("samples\tdft\tfft")
    for i in range(15):

            samples = 2**i

            # DFT processing time
            start = time.time()
            dft(signal[:samples])
            end = time.time()

            dft_time = end - start

            # FFT processing time
            start = time.time()
            np.fft.fft(signal[:samples])
            end = time.time()

            fft_time = end - start

            print(f"{samples}\t{dft_time}\t{fft_time}")
