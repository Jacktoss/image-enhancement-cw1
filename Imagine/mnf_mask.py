import math
import cmath
import numpy as np


# adding guassiana notch filter (maybe)

'''
star_coords[c][0] = "x"
star_coords[0][c] = "y"

r = "D0"

'''

def multi_nf(h, w, star_coords, rad):
    blank_mask = np.ones((h, w), dtype=float)
    star_coords.remove([h // 2, w // 2])

    for c in range(len(star_coords)):
        for i in range(h):
            for j in range(w):
                '''
                
                namely the distinction between u and v and u_0 v_0
            
    
                '''

                sq_Distance = (i - star_coords[c][0])**2 + (j - star_coords[c][1])**2
                # distance from

                gauss = 1 - math.exp(-sq_Distance / (2 * (rad**2)))
                # watch out for the bidmas/bodmas order of operations in realtion to brackets


                blank_mask[i][j] = blank_mask[i][j] * gauss
                # given our table is already filled with 1's


    return blank_mask


