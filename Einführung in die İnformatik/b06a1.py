

def gerade_summe(n: int)-> int:
    if n==1:
        return 2
    else:
       return n*2 + gerade_summe(n-1)

print(gerade_summe(5))