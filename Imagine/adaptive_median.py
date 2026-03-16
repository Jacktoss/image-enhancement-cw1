import math
import cmath

import numpy as np


def a_median(x, max_pad):

    '''
    Adaptive Median filter (level A/B)
    For every pixel the window crosses over it will be passed through 
    one of two levels.

    Before deciding which level the pixel will go down, the lowest and highest
    pixel in the current window must be known as well as the center value
    and median value.

    The first level 'A' checks if the median value of all the pixels in window
    is both greater than the lowest value and less than the highest value.
    This checks if the median value is a outlier/ extreme value because
    if it is then its likely static. If it is within the bounds then qualifies 
    to level 'B'. If it doesnt then the window size will increase and the
    first level check is repeated again this time with a new wider set of data.
    This can repeat until it hits the user specified maximum.

    If the condition ever becomes true for the pixel then level 'B' in
    this filter checks if the center pixel of the window is greater than
    the minimum pixel value and the maximum pixel value. If it meets this check
    then it passes because the center pixel is reasonable and not likely static
    given that a window of pixels around it has been taken into account so no
    change is made and the filter moves the window to the next pixel. If it
    does fail the condition then the next most reasonable option which is
    the median that was static checked in level A 

    Iterating on padded array so window isnt out of bounds.
    Subarray ending row/col index is exclusive and the starting it inclusive
    so +1 for the end of row/col index for subarray extraction
    '''
    

    x_p = np.pad(x, max_pad, mode='edge')   # using maximum pad first because is ensures recursive
    #doesnt cause index error
    xp_h, xp_w = np.shape(x_p)

    i, j = 0, 0
    for r in range(max_pad, xp_h - max_pad):
        for c in range(max_pad, xp_w - max_pad):
        
            pad_num = 1 # recursive process reseting pad_num
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

    '''
    recursive function to redo the filter condtions check
    for the new windwo size. Can continue forever because the max_pad
    parameter also pads the area to suit windows placed on edge pixels

    x is local scope
    '''

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



























































































































