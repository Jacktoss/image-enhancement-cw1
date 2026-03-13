from PIL import Image
import numpy as np
from working_fft import fft_2d_image
from fft_shift import fft_shift
from mag_spec import mag_spec
import matplotlib.pyplot as plt
from first_mask import create_mask1
from second_mask import create_mask2
from third_mask import create_mask3
from ifft_shift import ifft_shift
from working_ifft import ifft_2d_image

photo_orig = Image.open('../dogDistorted.bmp') 

# convert pixel values to greyscale and 2d list
photo_grid = np.array(photo_orig.convert('L')).tolist()

og_rows, og_cols = np.shape(photo_grid)

frequency_domain = fft_2d_image(photo_grid)

frequency_domain = fft_shift(frequency_domain)

magnitude_spectrum = mag_spec(frequency_domain)
#print(magnitude_spectrum)
#print(frequency_domain)

ms_np = np.array(magnitude_spectrum)


# rows // 2  and cols // 2 as coords = center
# if value is 12 < then prbably a star point or pont or collection
# of points more likely

'''
ok so kindof wokring but not. so some stars have like a max
of 12 as the brightest. however other have 12 as a low birhgtnes
value so there are hundrresds of +12 points on the grid
though i am starting to see a pattern

for one there are always  5 stars with the same axis value

given a snipped i think i can retroacdtivley (with the matplot diagram)


sweet spot it 12.2 kinda

I could just pick the heaviest axies?
x-axis
52
154
256 = centre
358
460

y-axis
cba to do yaxi also there isnt a single row or col coord that differs too much from these


given i found 256 had the most values over 12.21 confirms that the heaviest
does equal the center coord 

102 differndce up or down from center

103 difference from surroundng to outer stars

not too much 


print(np.argwhere(ms_np > 12.21))


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

show = mag_spec(fd_cmnf_applied)



fd_ishifted = ifft_shift(fd_cmnf_applied)

in_mat = ifft_2d_image(fd_ishifted, og_rows, og_cols) 




#after ifft
#img_cropped = in_np[0:og_rows, 0:og_width]

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



fd_unshifted = ifft_shift(fd_cmnf_applied) # Or use np.fft.ifftshift if you use numpy
# 3. Inverse FFT
in_np = np.fft.ifft2(fd_unshifted)
in_np = in_np.real

'''
np_o = np.array(in_mat)
Image.fromarray(np_o).convert('L').save('output.png')

