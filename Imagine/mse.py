import numpy as np
from PIL import Image

def calculate_mse(imageA, imageB):
    """
    Calculates the Mean Squared Error between two image arrays.
    Lower MSE indicates higher similarity.
    """
    imgA = np.array(imageA, dtype='float')
    imgB = np.array(imageB, dtype='float')
    err = np.sum((imgA - imgB) ** 2)
    mse = err / float(imgA.shape[0] * imgA.shape[1])
    
    return mse

if __name__ == "__main__":
    try:
        original_img = Image.open('../DogOriginal.bmp').convert('L')
        # Load the output from your filters
        filtered_img = Image.open('test_output.bmp').convert('L') 
        
        mse_value = calculate_mse(original_img, filtered_img)
        print(f"Mean Squared Error: {mse_value:.2f}")
        
    except FileNotFoundError as e:
        print(f"File not found. Please check paths. Details: {e}")
