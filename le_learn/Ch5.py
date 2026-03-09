import cmath
import math

from Ch2 import dft

def fft_one_level(x):

    N = len(x)

    if (N == 1):
        return x
    
    x_even = x[0::2]
    x_odd = x[1::2]

    E = fft_one_level(x_even)
    O = fft_one_level(x_odd)


    out_list = [0] * N

    for k in range(int(N/2)):
        w = cmath.exp(-2j * math.pi * k / N)
        out_list[k] = E[k] + w * O[k]
        out_list[k + N//2] = E[k] - w * O[k]

    
    return out_list


y = [1.0, 2.0, 3.0, 4.0]

def fft_2D(x):

    #given a 2d grid of numbers (square)
    #
    output_1 = [[0]*len(x) for _ in range(len(x[0]))]
    output_2 = [[0]*len(x) for _ in range(len(x[0]))]
    
    for row in range(len(x)):
        output_1[row] = fft_one_level(x[row])
        for col in range(len(x)):
            output_2[col][row] = output_1[row][col]
    
    for row in range(len(x)):
        output_2[row] = fft_one_level(output_2[row])
    
    for row in range(len(x)):
        for col in range(len(x)):
            x[col][row] = output_2[row][col]




    return x





def ifft_one_level(x):

    N = len(x)

    if (N == 1):
        return x
    
    x_even = x[0::2]
    x_odd = x[1::2]

    E = ifft_one_level(x_even)
    O = ifft_one_level(x_odd)


    out_list = [0] * N

    for k in range(int(N/2)):
        w = cmath.exp(2j * math.pi * k / N)
        out_list[k] = E[k] + w * O[k]
        out_list[k + N//2] = E[k] - w * O[k]

    


    out_list = [i / N for i in out_list]

    return out_list






























