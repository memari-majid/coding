def search(pat, str):
    patt_len = len(pat)
    str_len = len(str)
    for i in range(str_len - patt_len + 1):
        j = 0
        while j < patt_len:
            if str[i + j] != pat[j]:
                break
            j += 1
        if j == patt_len:
            print(f'{pat} found starting at {i}')


if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)

