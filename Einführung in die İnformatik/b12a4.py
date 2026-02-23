

def maxmult_lin(L):
    if len(L) < 2:
        return 0

    max1 = 0
    max2 = 0

    for x in L:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x

    return max1 * max2
