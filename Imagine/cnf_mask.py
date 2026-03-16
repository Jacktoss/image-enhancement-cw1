import math
import cmath
import numpy as np



def custom_nf(h, w, s_l1, rad_dc, star_space, rad_other=0):
    # c_coords are to be of the center a.k.a. dc component 
    # added space between stars as a parameter

    '''
    aims to cut out the grid shaped noise on the frequency domain
    Grid intensity goes up the closer to any star, weakes when
    further way from any start

    s_l1 being array of star components. Places lines on the grid lines
    of noise. Every noise spike
    has a symetrical copy of itself and so line up with only with every 
    other star component (either x or y). For 25 locations using only
    5 components.

    checks for every pixel in the line is in the range of the mask radius
    of the mult-notch frequency mask applied before this. 

    This filter uses its usefulness the higher the other notch filter
    setting is.


    This loops through each star components then along each new blank_line
    but also makes sure to skip each star location (only component because
    its 1d only) with a notch on it and its radius.

    star_space refering to distance between 2 noise spikes which is the same
    for all of them.

    rad_dc the precieved radius of the DC component noise
    
    checks if current line is one of the 2 that goes throught the DC component
    and checks if in range of it. Aiming to avoid it

    Butterworths formula used because smooth transition from gausian
    less impactful given 1D space of pixels. Also because lines
    fade less than other noise from spike/star.
    This one more polynomial roll-off.
    
    result = 1 / (1 + (radius / distance)^(2n))
    
    the radius being half the distance to a star

    '''
    star_fade = star_space / 2

    blank_mask = np.ones((h, w), dtype=float)
    go = True
    for star in range(len(s_l1)):
        blank_line = np.ones((h), dtype=float)
        for i in range(len(blank_line)):
            go = True
            for j in range(len(s_l1)):
                if s_l1[j] - rad_other <= i <= s_l1[j] + rad_other:
                    go = False
                    break
            if not go:
                continue

            if s_l1[star] == h//2 and h//2 - rad_dc <= i <= h//2 + rad_dc:
                continue
            
            # minimum absolute distance from the closest star
            closest_star = min(s_l1, key=lambda x: abs(x - i))
            distance = abs(i - closest_star)
            # given its a 1d array not a 2d one butterworth method more suited
            n = 0.4 
            butterworth = 1.0 / (1.0 + (star_fade / distance)**(2 * n))

            blank_line[i] = blank_line[i] * butterworth 

            if s_l1[star] == h//2:
                # if the line passes through dc component then it also
                # gains noise from the dc componenet iself, here I aim
                # to reduce the line noise once more while not changing
                # anything too close to it.
                distance_dc = abs(i - h//2)
                n = 0.4 
                butterworth_dc = 1.0 / (1.0 + ((h//2) / distance_dc)**(2 * n))
                blank_line[i] = blank_line[i] * butterworth_dc

        # placint lines from 2 sides so they overlap (but not over each other)
        blank_mask[s_l1[star], :] = blank_line
        blank_mask[:, s_l1[star]] = blank_line

    return blank_mask
    




    



























































































































































































































































































































































































































































































































































