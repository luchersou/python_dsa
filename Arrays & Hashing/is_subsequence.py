def is_subsequence(s, t):
    i = 0  # ponteiro em s
    
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    
    return i == len(s)