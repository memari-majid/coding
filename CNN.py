




def conv2D(img, kernel, s):
    w = len(img)
    k = len(kernel)
    o = int(((w - k) / s) + 1)
    output = [[0] * w for i in range(w)]
    for i in range(w):
        if i > w - k: break
        if i % s == 0:
            for j in range(w):
                if j > w - k: break
                if j % s == 0:
                    output[i, j] = (kernel * img[i:i + k, j:j + k]).digit_sum()
    return output
