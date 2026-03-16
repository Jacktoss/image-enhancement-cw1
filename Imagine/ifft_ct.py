
import math
import cmath

'''
similar to fft_ct.py but changing exponent sign

Requires normalisation factor dividing every element by the product
of the rows and columns. FFT sums up contributions and scales them up
(when doing fft over rows then columns)

After masks there will be residual imaginary parts but still near zero.
.real drops them
'''

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
    
    return out_list


def transpose_2d(matrix):

    return list(map(list, zip(*matrix)))   # map() returns map objects 


def ifft_2d_image(image_matrix, og_height=None, og_width=None):
    
    if og_height is None or og_width is None:
        raise ValueError("IFFT needs original height and width of image to remove padding. Otherwise add 2 parameters of 0 to continue without de-padding")
    
    rows = len(image_matrix)
    cols = len(image_matrix[0])

    for row in range(rows):
        image_matrix[row] = ifft_one_level(image_matrix[row]) 

    image_matrix = transpose_2d(image_matrix)

    for col in range(cols):
        image_matrix[col] = ifft_one_level(image_matrix[col])

    image_matrix = transpose_2d(image_matrix)

    for i in range(rows): 
        for j in range(cols):
            image_matrix[i][j] = (image_matrix[i][j] / (rows * cols)).real 
    #only real

    if og_height == 0 and og_width == 0:
        return image_matrix
    
    crop_matrix = []

    for i in range(og_height): #removes padding ignoring excess hight if any
        crop_matrix.append(image_matrix[i][0:og_width])

    return crop_matrix  






























































