

#bo84

def gitter_wege(m, n, wb):

    if (m, n) in wb:
        return wb[(m, n)]

    if m <= 0 or n <= 0:
        return 0

    # basis
    if m == 1 or n == 1:
        return 1


    wege = gitter_wege(m - 1, n, wb) + gitter_wege(m, n - 1, wb)
    wb[(m, n)] = wege

    return wege

m = int(input("m: "))
n = int(input("n: "))

print(gitter_wege(m, n, {}))
