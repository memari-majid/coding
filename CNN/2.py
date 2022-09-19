import numpy as np


def calculate_target_size(img_size: int, kernel_size: int) -> int:
    num_pixels = 0
    for i in range(img_size):
        # Add the kernel size to the current i
        added = i + kernel_size
        # It must be lower than the image size
        if added <= img_size:
            # Increment if so
            num_pixels += 1
    return num_pixels


def convolve(img: np.array, kernel: np.array) -> np.array:
    # Assuming a rectangular image
    output_size = calculate_target_size(
        img_size=img.shape[0],
        kernel_size=kernel.shape[0]
    )
    k = kernel.shape[0]
    convolved_img = np.zeros(shape=(output_size, output_size))

    for i in range(output_size):
        for j in range(output_size):
            current_matrix = img[i:i + k, j:j + k]
            convolved_img[i, j] = np.sum(np.multiply(current_matrix, kernel))
    return convolved_img
