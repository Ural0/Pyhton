

def zerfall(n, p, t):

    if t == 0:
        return float(n)
    else:
        übrig = n - (n * p / 100)
        return zerfall(übrig,p,t-1)



print(zerfall(200, 50, 0))
print(zerfall(200, 50, 1))
print(zerfall(200, 50, 4))
print(zerfall(180.9, 17, 2))
