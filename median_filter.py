import math
import cmath

import numpy as np



def med_filter(x, win):
    '''
    similar to mean filter but how would it 
    be done differently this time


    i could loop through a sub array or use a loop recurvie thing
    e.g. arr[1:4, 2:5] aimin at index row 2 and column 3 (exclusive of later, inclusive of former)
    with pad num 1

    then np.sort(subarray)


    np.median(subarra) exists

    '''
    pad_num = win // 2

    x_p = np.pad(x, pad_num, mode='constant', constant_values=0)

    xp_h, xp_w = np.shape(x_p)
    i, j = 0, 0
    for r in range(pad_num, xp_h - pad_num):
        for c in range(pad_num, xp_w - pad_num):

            x[i, j] = np.median(x_p[(r-pad_num):(r+pad_num+1), (c-pad_num):(c+pad_num+1)])

            j += 1
        
        i += 1
        j = 0
    
    return x

































































