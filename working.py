from PIL import Image
import numpy as np
from working_fft import fft_2d_image
from fft_shift import fft_shift
from mag_spec import mag_spec
import matplotlib.pyplot as plt
from first_mask import create_mask


photo_orig = Image.open('../dogDistorted.bmp') 

# convert pixel values to greyscale and 2d list
photo_grid = np.array(photo_orig.convert('L')).tolist()

frequency_domain = fft_2d_image(photo_grid)

frequency_domain = fft_shift(frequency_domain)

magnitude_spectrum = mag_spec(frequency_domain)

#print(frequency_domain)

ms_np = np.array(magnitude_spectrum)

# rows // 2  and cols // 2 as coords = center
# if value is 12 < then prbably a star point or pont or collection
# of points more likely

'''

'''

s_l1 = [51,154,256,358,462]

#star_coords = [[0 for _ in range(5)] for _ in range(5)]
star_coords = []
for i in range(5):
    for j in range(5):
        star_coords.append([s_l1[i], s_l1[j]])

#print(star_coords)

show = create_mask(512, 512, star_coords, 5)


'''

plt.figure(figsize=(8, 8))
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("shifted mag spec")
plt.axis('on')
plt.show()

'''




plt.figure(figsize=(8, 8))
plt.imshow(show, cmap='gray')
plt.title("cumc")
plt.axis('on')
plt.show()





























