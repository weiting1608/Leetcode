def kmpSearch(pat, txt):
    N = len(txt)
    M = len(pat)
    # lps means the longest prefix array which is also a suffix
    lps = [0] * M
    computeLPSArray(pat, M, lps)
    i, j = 0, 0 # i for txt, j for pat
    while i < N-M+1:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            # lps[j-1] means before the mismatch happens at pat[j], how many characters are suffix and prefix,
            # so that you can just update j with this value and compare the jth position of pat, 
            # no need to compare the previous one.
            if j != 0:
                j = lps[j-1]
            # meaning mismatch happens at the 0th of pat, then only increment i.
            else:
                i += 1
        if j == M:
            return i-j
            j = lps[j-1] # when found one match, reset j to continue searching

def computeLPSArray(pat, m, lps):
    # two pointers, len means the length of longest prefix & suffix. i is for iterate.
    len = 0
    i = 1
    lps[0] = 0
    while i < m:
        if pat[i] == pat[len]:
            lps[i] = len + 1
            len += 1
            i += 1
        else:
            if len != 0:
                len = lps[i-1]
            else:   
                lps[i] = 0
                i += 1
            # reset len, necessary for the pattern which has broken


    
