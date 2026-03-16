import matplotlib.pyplot as plt

def display_ms(magnitude_spectrum):

    plt.figure(figsize=(8, 8))
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title("shifted mag spec")
    plt.axis('on')
    plt.show()

