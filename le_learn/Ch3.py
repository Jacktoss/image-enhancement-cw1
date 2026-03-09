import cmath
import math

from Ch2 import dft

def fft_one_level(x):

    N = len(x)

    x_even = x[0::2]
    x_odd = x[1::2]

    E = dft(x_even)
    O = dft(x_odd)


    out_list = [0] * N

    for k in range(int(N/2)):
        w = cmath.exp(-2j * math.pi * k / N)
        out_list[k] = E[k] + w * O[k]
        out_list[k + N//2] = E[k] - w * O[k]



    
    return out_list


y = [1.0, 2.0, 3.0, 4.0]

#print(fft_one_level(y))





















































