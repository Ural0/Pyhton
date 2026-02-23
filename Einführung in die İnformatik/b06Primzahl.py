
def primzahlen(n: int)->list:
    if n == 1:
        return []
    elif n==2:
        return [2]
    else:
        if n % 2 == 0:
            return primzahlen(n - 1)
        else:
            n
            return primzahlen(n - 1) ,n
    print(n)

print(primzahlen(8))