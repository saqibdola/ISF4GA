

def remainder(i, line1, line2):
    rem = (i+1) % 3
    if rem == 0:
        asdf = line1[i - 2:i + 1]
        asdfg = line2[i - 2:i + 1]
    elif rem == 1:
        asdf = line1[i:i + 3]
        asdfg = line2[i:i + 3]
        print('rem', asdf)
    else:
        asdf = line1[i - 1:i + 2]
        asdfg = line2[i - 1:i + 2]
    return asdf, asdfg