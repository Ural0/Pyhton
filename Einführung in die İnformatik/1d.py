
def f(n):
    if n<0:
        return False
    return f(3*n-6)

print(f(4))

