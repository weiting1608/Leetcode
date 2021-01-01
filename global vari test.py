lps = []
def test():
    global lps
    lps[0] = 1

test()
for i in range(len(lps)):
    print(lps[i])
