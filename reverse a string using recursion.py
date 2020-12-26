# Reverse a string using recursion

def reverse(s):
    # base case
    if len(s) == 1:
        return s
    
    # wrong: the simple, s[:len(s)-1] make more calls
    # output is fedcbaedcbadcbacbabaa 
    # return s[::-1] + reverse(s[:len(s)-1])

    # right:
    return reverse(s[1:]) + s[0]

s = "abcdef"
print(reverse(s))