def search(pattern, string):
    patt_len = len(pattern)
    str_len = len(string)
    for i in range(str_len - patt_len + 1):
        j = 0
        while j < patt_len:
            if string[i + j] != pattern[j]:
                break
            j += 1
        if j == patt_len:
            print(f'{pattern} found starting at {i}')


if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)

