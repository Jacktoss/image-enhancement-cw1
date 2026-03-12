from PIL import Image
import numpy as np
from working_fft import fft_2d_image
from fft_shift import fft_shift
from mag_spec import mag_spec
import matplotlib.pyplot as plt
from first_mask import create_mask1
from second_mask import create_mask2
from third_mask import create_mask3

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

s_l1 = [51,154,256,358,461] # list of either possible x or y values of target noise
# the space between them being 102 or 103

#star_coords = [[0 for _ in range(5)] for _ in range(5)]
star_coords = []
for i in range(5):
    for j in range(5):
        star_coords.append([s_l1[i], s_l1[j]])

#print(star_coords)

#mnf_mask = create_mask2(512, 512, star_coords, 5)

#radius of dc noise is about 75
cnf_mask = create_mask3(512, 512, s_l1, 75, 102, 5)

mnf_mask = create_mask2(512, 512, star_coords, 5)

fd_np = np.array(frequency_domain)


#fd_mnf_applied = fd_np * mnf_mask
#fd_cnf_applied = fd_np * cnf_mask

fd_cmnf_applied = fd_np * mnf_mask * cnf_mask

# Matplotlib cannot show complex number but can show are mag spectrum of the masked fd iamge

#show = mag_spec(fd_cmnf_applied)




'''
plt.figure(figsize=(8, 8))
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("shifted mag spec")
plt.axis('on')
plt.show()



plt.figure(figsize=(8, 8))
plt.imshow(show, cmap='gray')
plt.title("cumc")
plt.axis('on')
plt.show()

'''



fd_unshifted = fft_shift(fd_cmnf_applied) # Or use np.fft.ifftshift if you use numpy
# 3. Inverse FFT
in_np = np.fft.ifft2(fd_unshifted)
in_np = in_np.real

Image.fromarray(in_np).convert('L').save('output.png')



































