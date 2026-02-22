

def f(n: int):
    i = 5
    j = 3

    while i != j or n < i:
        i = 222** j - 12   # (operatör çok önemli değil burada)
        j = i + 1
        n = i - 1

    return j

print(f(7))