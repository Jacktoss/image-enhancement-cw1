import math
import cmath

import numpy as np





def mean_filter(x, win):
    '''
    '''
    if win % 2 == 0 or win < 3 : return -1

    pad_num = win // 2
    
    x_p = np.pad(x, pad_num, mode='constant', constant_values=0)

    xp_h, xp_w = np.shape(x_p)
    i, j = 0, 0
    for r in range(pad_num, xp_h - pad_num):
        for c in range(pad_num, xp_w - pad_num):

            x[i, j] = np.mean(x_p[(r-pad_num):(r+pad_num+1), (c-pad_num):(c+pad_num+1)])
            # pad is the half of window reaches end of window from r,c. +1 as later pair vlaue
            #is exclusive former is inclusive

            j += 1
        
        i += 1
        j = 0


    return x








'''
    x_p = np.pad(x, pad_num, mode='constant', constant_values=0)

    xp_h, xp_w = np.shape(x_p)

    i, j = 0, 0
    for r in range(pad_num, xp_h - pad_num):
        
        for c in range(pad_num, xp_w - pad_num):
            
            x[i, j] = (
                x_p[r+1, c] +
                x_p[r+1, c+1] +
                x_p[r, c+1] +
                x_p[r-1, c+1] +
                x_p[r-1, c] +
                x_p[r-1, c-1] +
                x_p[r, c-1] +
                x_p[r+1, c-1] +
                x_p[r, c]
            ) / 9

            j += 1
        i += 1
        j = 0
'''


'''
alot cleaner and less complex using numpy subarray slicing

'''



















































