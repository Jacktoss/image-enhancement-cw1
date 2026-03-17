## METHODOLOGY ##

Any signal can be recreated by adding together sinusodial waves of differnt frequencies, amplitudes and
phases. Cosine wave being the real part and sine wave the imaginary part.
The reason for using a fast-fourier transform is because it extracts frequency components from the image.
Transforming the image from spatial to frequency domain (the Fourier).
Because of this FFT can be used in a range of applications like image analysis, filtering, reconstruction 
and compression.

For our implemenation I will use the Cooley-Tukey version of the FFT because it is less time complex
becasue of its recursive divide-and-conquer approach.
Cooley-Tukey fft will be taking a 1D array and be applied to every row and every column to in-effect
achieve a 2D fft. First it splits the array of length N into even and odd indexed values of length N/2 each.
When doing this it effectively shifts odd pixels by one, so they line up with even ones for cacluation.
Thie requires a rotation of the odd waves phase to account for this later.
The function is recursively called on both arrays; this happens again until the length
of each array is 1 for which the base case returns that single value because the frequency representation
is just the pixel value itself. As the recursion returns up the results of both the even
and odd halves are combined to form the full frequency spectrum, only after the odd ones
have been multiplied by the twiddle factors.

complete frequency[k] = even frequency[k] + (twiddle * odd frequency[k])

Adding and subtraction can be done because sine and cosine waves repeat themselves. So 
a frequency wave at k + N/2 is the same as a frequency wave at k but upside down. So, k only increases
to N/2 because we already have the rest of the frequency spectrum for this list just flip the 
sign of w * O[k]

```python
    for k in range(int(N/2)): 
        w = cmath.exp(-2j * math.pi * k / N)
        out_list[k] = E[k] + w * O[k]         # first half
        out_list[k + N//2] = E[k] - w * O[k]  # second half
    return out_list
```
Time complexity from standard DFT for the same list O(N^2) to O(N log N) length N.

When it comes to a 2D version of this I applied the 1D function on 2 axis. Running it across
every row then transforming the image horizontally, essentialy swapping the rows for collumns
then appling the function to every row (column of the original). Then transposing it again
returning it to its original positioning but holding different values.

Because the algorithm requires every row/col to be divided down to single values, the original
image must be a power of 2 which pad_image() handles.


==== too much compress it down


====


Explain fft_shift design+process+implementation



Explain magnitude spectrum design+process+implementation

Gaussian Multi-Notch Reject Filter (mnf_mask) design+process+implementation

Custom Slit/Grid Filter (cnf_mask) design+process+implementation

Mean + Median Filter design+process+implementation

Alpha-trimmed mean filter design+process+implementation

Adaptive median filter design+process+implementation

Expalin your chosen pipeline at_mean(3) -> a_median(3)
