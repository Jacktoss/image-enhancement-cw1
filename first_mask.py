import math
import cmath
import numpy as np


# multi notch mask (probably)

'''
lets start with a 5 for now
and ignore the uh center


the logic i think i know dont know how to implement.

not executing mask here aint no way

'''

def create_mask(h, w, star_coords, rad):
    blank_mask = np.ones((h, w), dtype=float)
    star_coords.remove([h // 2, w // 2])

    for c in range(len(star_coords)):
        for i in range(h):
            for j in range(w):

                if ((i - star_coords[c][0])**2 + (j - star_coords[c][1])**2 <= rad**2):
                    blank_mask[i][j] = 0
    
    return blank_mask.tolist()




