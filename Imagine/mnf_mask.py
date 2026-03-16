import math
import cmath
import numpy as np

'''
Gausian give a smooth roll off effect, reminded me of the white noise I saw in fd

Circle shaped notches that are placed on the spikes of noise or "stars"
Conditional avoids the center because its the DC component now centered from the shift

The gaussian value at any point within the notch circle is one minus the 
exponential of the negative squared distance divided by two radius.

c^2 = a^2 + b^2 
where a is the x-difference between point and star
where b is the y-difference between point and star


For every "mask" starts with a proportional sized array of 1s because
its has no effect when multiplied by the image.

'''
def multi_nf(h, w, star_coords, rad):
    blank_mask = np.ones((h, w), dtype=float)
    
    for c in range(len(star_coords)):
        if star_coords[c][0] == h // 2 and star_coords[c][1] == w //2:
            continue
        for i in range(h):
            for j in range(w):
                sq_Distance = (i - star_coords[c][0])**2 + (j - star_coords[c][1])**2
                # distance from star

                gauss = 1 - math.exp(-sq_Distance / (2 * (rad**2)))
                # watch out for the bidmas/bodmas order of operations in realtion to brackets

                blank_mask[i][j] = blank_mask[i][j] * gauss
                # given our table is already filled with 1's
    return blank_mask


