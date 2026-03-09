import cmath
import math


#mult by 180/pi to convert radians to degrees, a full circle is 2pi. unit circle
#a point anywhere in that space (on the circle is in format a + bj)

def roots_of_unity(N): 

    #theta = 2 * math.pi / N
    #if (N == 1):
    #    return 1 + 0j
    
    results = []

    if (N < 1):
        return 0

    
    
    

    for k in range(N):
        #theta = 2 * math.pi * k+1 / N
       
        #results.append(cmath.cos(theta) + icmath.cos(theta))
        results.append(cmath.exp(2j * math.pi * k / N))

    return results

    
print(roots_of_unity(1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      