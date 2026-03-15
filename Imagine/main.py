import os

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt  #show magnitude spectrum
import tkinter
from tkinter import Tk, filedialog


from fft_ct import fft_2d_image
from fft_shift import fft_shift
from mag_spec import mag_spec
from mnf_mask import multi_nf
from cnf_mask import custom_nf
from ifft_shift import ifft_shift
from ifft_ct import ifft_2d_image
from mean_filter import mean_filter
from median_filter import median_filter
from alpha_trim_mean import at_mean
from adaptive_median import a_median
from mse import calculate_mse

from magnitude_frequency_test import display_ms
from frequency_domain_mask_test import display_masked_fd





root = Tk() # initialise tkinter gui toolkit for file dialogs

root.withdraw() # hides main tkinter window


'''
tkinter for easier file selection
prompt filedialog to ask for file, note distorted image must be chosen first

'''


distorted_path = filedialog.askopenfilename(title="Select distorted image")

print(f"Obtained distorted at {distorted_path}" + "\n")

photo = Image.open(distorted_path)

original_path = filedialog.askopenfilename(title="Select original image")

print(f"Obtained original at {original_path}" + "\n")

photo_o = Image.open(original_path)

file_path = os.path.dirname(distorted_path)

res = input(f"Would you like output saved? Yes:[Y] No:[N]" + "\n")
res = res.strip().lower()
if res == 'y':
    user_path = filedialog.askdirectory(title="Select output directory")
elif res == 'n':
    user_path = None
else:
    raise ValueError("Invalid Input")

print('Loading... ' + '\n')
photo_grid = np.array(photo.convert('L')).tolist() # convert pixel values to greyscale and 2d list for my fft
photo_o_grid = np.array(photo_o.convert('L'))

og_rows, og_cols = np.shape(photo_grid)


frequency_domain = fft_2d_image(photo_grid)
frequency_domain = fft_shift(frequency_domain)


magnitude_spectrum = mag_spec(frequency_domain)


ms_np = np.array(magnitude_spectrum)

'''
To show magnitude spectrum:
display_ms(ms_np)


Looking closely at the magnitude spectrum the noise spikes seem to all
be on the same y axis or x axis depending where they are almost like a grid

x-axis
52
154
256 = centre
358
460

Picked from visual observance of the magnitude spectrum's noise spikes
The noise spike was the heaviest at the center of 256,256 (magnitude frequency)
which is the DC component of which must not be changed because it will affect
the brightenss of the entire image. The fft shift earlier concentrated the component to
one point so it is easer to avoid when making masks for the frequency domain

'''

s_l1 = [51,154,256,358,461] #star coordinate components

'''
Given A star coordinate on the magnitude/frequency spectrum can only be 
made up of 2 of the values It would be safe to create a nested for loop to create
all 25 of their locations.
e.g. star_coords = [[0 for _ in range(5)] for _ in range(5)]
'''

star_coords = []
for i in range(5):
    for j in range(5):
        star_coords.append([s_l1[i], s_l1[j]])

fd_np = np.array(frequency_domain) 

'''
I measured the radius of dc component noise is about 75 using the magnitude frequency.

After testing different size or in this case radius of the multi-notch frequency
mask, 25 seemed to produce the best results on the final image. (subject to change)

The custom notch frequency mask I made aimed to go after the white grid lines.
Not sure if it is/was a mistake

cnf_mask needing both the distance between stars and the radius of the first
mask because it works directly over them and the stars while also making sure
to avoid the DC component's noise

'''

mnf_mask = multi_nf(512, 512, star_coords, 40) # Multi-notch frequency mask
# make sure the last parameter is the same for both.
cnf_mask = custom_nf(512, 512, s_l1, 75, 102, 40) # Custom-notch frequency mask


fd_cmnf_applied = fd_np * mnf_mask * cnf_mask


# cannot show complex number, only real values from magnitude spectrum
show = mag_spec(fd_cmnf_applied)





fd_ishifted = ifft_shift(fd_cmnf_applied)

in_mat = ifft_2d_image(fd_ishifted, og_rows, og_cols) 
'''

To show effects on frequency spectrum
display_masked_fd(show)
ifft requires the original image dimensions because it depads its from when it was
oringinaly padded so dimensions where powers of 2. to perform the cooley-tukey fft algorithm

ifft_2d_image return .real

will be something like
img_cropped = in_np[0:og_rows, 0:og_width]

ifft_2d_image returns a normal python array 


feel free to try out mean and median filters!

Filters of standard mean and median:
np_o = mean_filter(np_o, 3)
np_o = med_filter(np_o, 3)

parameter in Adaptive Median Filter is maximum padding value 
rather than window size. So 3 means window of 9.

I find both work well together when set at 3 for each

The Mean Squared Error measuring the average squared difference between
corresponding values between a original and processed image. The lower it is
the higher the similarity with 0 being identical.
'''

np_o = np.array(in_mat)

np_o = at_mean(np_o, 3) # Alpha Transform Mean filter

np_o = a_median(np_o, 3) # Adaptive Median Filter

mse = calculate_mse(photo_o, photo)
mse1 = calculate_mse(photo_o, np_o)


print(f"MSE Distorted vs Original = {mse}")
print(f"MSE Enhanced Distorted vs Original = {mse1}")



if user_path: Image.fromarray(np_o).convert('L').save(os.path.join(user_path, 'output.bmp'))











