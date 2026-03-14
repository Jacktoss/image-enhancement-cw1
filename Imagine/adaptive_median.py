import math
import cmath

import numpy as np



'''
'''


def a_median(x, max_pad):

    x_p = np.pad(x, max_pad, mode='edge')   # using maximum pad first because is ensures recursive
    #doesnt cause index error


    xp_h, xp_w = np.shape(x_p)

    i, j = 0, 0
    for r in range(max_pad, xp_h - max_pad):
        for c in range(max_pad, xp_w - max_pad):
        
            pad_num = 1 # recursive process has to work up to max_pad
            p_win = x_p[(r-pad_num):(r+pad_num+1), (c-pad_num):(c+pad_num+1)]
            p_min = np.min(p_win)
            p_max = np.max(p_win)
            p_med = np.median(p_win)

            if p_min < p_med < p_max: # adaptive median filter logic
                if p_min < x[i, j] < p_max:
                    pass
                else:
                    x[i, j] = p_med
            else:
                cent_p = x[i, j]                
                x[i, j] = sub_med(x_p, r, c, pad_num+1, max_pad, cent_p)

            j += 1
        i += 1
        j = 0
    
    return x


# pad_num will be +1
#



def sub_med(x, r, c, pad_num, max_pad, cent_p):

    p_win = x[(r-pad_num):(r+pad_num+1), (c-pad_num):(c+pad_num+1)]
    p_min = np.min(p_win)
    p_max = np.max(p_win)
    p_med = np.median(p_win) #pasted from a_median

    
    if p_min < p_med < p_max:
        if p_min < cent_p < p_max:
            return cent_p
        else:
            return p_med
    else:  # logic of adaptive median filter levels A and B
        if pad_num == max_pad:
            return p_med
        else:
            return sub_med(x, r, c, pad_num+1, max_pad, cent_p)



























































































































