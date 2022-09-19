import numpy as np


def conv2D(img, kernel, s):
    w = len(img)
    h = len(img[0])
    k = len(kernel)
    p = (len(kernel) - 1) / 2
    o = int(((w - k + 2 * p) / s) + 1)
    output = np.zeros((o, o))
    if p != 0:
        img = np.zeros((w + p * 2, h + p * 2))
        img[int(p):int(-1 * p), int(p):int(-1 * p)] = img
    for i in range(w):
        if i > w - k: break
        if i % s == 0:
            for j in range(h):
                if j > h - k: break
                if j % s == 0:
                    output[i, j] = (kernel * img[i:i + k, j:j + k]).digit_sum()
    return output
