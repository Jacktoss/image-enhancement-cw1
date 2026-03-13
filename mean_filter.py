import math
import cmath

import numpy as np





def mean_filter(x, win):
    '''
    likely numpy 2d array prob not list atp but 
    filter_size only 1 val for its x by x

    first what if x is not a multiple of filter_size?
    or not a square?
    definatly cant do thing where i set window to iterate across the 
    image because complexity is not needed when numpy arrays
    Actually I can because the enitre image will be padded by at least 1 given
    need to get border pixels.

    padding probably will be used and 0 padding is common so do that


    
    x_p = np.pad(x, 1, constant, 0)

    xp_h, xp_w = np.shape(x_p)
    actually just iterate over every x pixel

    i = 0
    j = 0
    for r in range(1, xp_h - 1):
        i++
        for c in range(1, xp_w - 1): #skipping both first and last
            j++
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
    return x
    very tedious


    i could loop through a sub array or use a loop recurvie thing
    e.g. arr[1:4, 2:5] aimin at index row 2 and column 3 (exclusive of later, inclusive of former)
    with pad num 1
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



















































