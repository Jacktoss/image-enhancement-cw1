
# FFT produces complex numbers magnitude and phase are extracted from them.
# for one complex number abz(z) for a array np.abs(array)
# magnitude = sqrt(real^2 + imaginary^2)
#
#
#
# Phase is where exactly in its cycle taht frequency starts. from a complex number phase = atan2(imaginary, real)
# in pythong np.angle(array)

# this is the radix2 version explaination of how it relates to fft:
#T.B.A.


"""
FFT is the first step that lets you fix the image.







"""

import numpy as np
from PIL import Image;

#img = Image.open("face.bmp")
#pixels = np.array(img)
#x = pixels

#pillows can also do img.show()
#


def fft(x): # 1D arrays
    lp = len(x); # shold be a power of 2
    
    if lp == 1:
        return x
    else:
        x_even = x[::2]  #even indexed numbersss. not necessarily even-numbered values
        x_odd = x[1::2]

        x_even = fft(x_even) #recursively work through both even and odd sections
        x_odd = fft(x_odd)

        e_value = np.exp(-2 * np.pi * 1j / lp)
        '''
        .exp()  a numpy source code in C
        Given a complex input for param a + bj

        Logic:
        .exp(a + bj = exp
        '''        

        k = np.arange(0, lp//2)#.reshape(-1, 1) # needing to create a column vector or not

        w = e_value**k

        x_odd = w * x_odd

        return np.concatenate( [x_even + x_odd, x_even - x_odd] )


import numpy as np

test = [1.0, 2.0, 3.0, 4.0]
my_result = fft(test)
np_result = np.fft.fft(test)

for i in range(len(test)):
    print(f"bin {i}: mine={my_result[i]:.4f}  numpy={np_result[i]:.4f}")

print(test)
