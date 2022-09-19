def search(str, pat):
    for i in range(len(str) - len(pat) + 1):
        if str[i:i + len(pat)] == pat:
            print(i)


if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(txt, pat)
