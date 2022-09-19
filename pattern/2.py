def KMPSearch(pat, str):
    patt_len = len(pat)
    str_len = len(str)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * patt_len
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, patt_len, lps)

    i = 0  # index for txt[]
    while i < str_len:
        if pat[j] == str[i]:
            i += 1
            j += 1

        if j == patt_len:
            print("Found pattern at index", str(i - j))
            j = lps[j - 1]

        # mismatch after j matches
        elif i < str_len and pat[j] != str[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

            # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain
