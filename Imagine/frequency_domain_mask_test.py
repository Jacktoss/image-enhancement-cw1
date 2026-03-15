import matplotlib.pyplot as plt


def display_masked_fd(show):


    plt.figure(figsize=(8, 8))
    plt.imshow(show, cmap='gray')
    plt.title("Effects from masks on Magnitude Spectrum")
    plt.axis('on')
    plt.show()