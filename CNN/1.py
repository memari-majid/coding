import numpy as np

def conv2D(image, kernel, padding, strides):
    # Most libraries implemented using cross-correlation
    # Cross Correlation = flipped Convolution
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernel = kernel.shape[0]
    yKernel = kernel.shape[1]
    xImage = image.shape[0]
    yImage = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImage - xKernel + 2 * padding) / strides) + 1)
    yOutput = int(((yImage - yKernel + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding * 2, image.shape[1] + padding * 2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through columns
    for y in range(image.shape[1]):
        # stop when y > 221
        if y > image.shape[1] - yKernel:break
        # beginning point jump by strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # x > 221
                if x > image.shape[0] - xKernel:break
                try:
                    # beginning point jump by strides
                    if x % strides == 0:
                        # element wise product
                        output[x, y] = (kernel * imagePadded[x: x + xKernel, y: y + yKernel]).sum()
                except:
                    break

    return output

kernel = np.random.randint(2,size=(3,3))
input = np.random.randint(2,size=(224,224))
