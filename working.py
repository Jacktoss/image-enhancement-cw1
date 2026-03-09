from PIL import Image
import numpy as np
from working_fft import fft_2d_image
from fft_shift import fft_shift
from mag_spec import mag_spec
import matplotlib.pyplot as plt


photo_orig = Image.open('../dogDistorted.bmp') 

# convert pixel values to greyscale and 2d list
photo_grid = np.array(photo_orig.convert('L')).tolist()

frequency_domain = fft_2d_image(photo_grid)

frequency_domain = fft_shift(frequency_domain)

magnitude_spectrum = mag_spec(frequency_domain)

#print(frequency_domain)

plt.figure(figsize=(8, 8))
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("shifted mag spec")
plt.axis('on')
plt.show()




















