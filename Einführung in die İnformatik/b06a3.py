

def zerlegung(w: str):
    if w == "":
        return []
    else:
        return [w[0:2]] + zerlegung(w[2:])
        #w[0:2] Es nimmt die ersten beiden Buchstaben + Weiter mit dem restlichen String


print(zerlegung("abcdef"))
print(zerlegung("abc"))
print(zerlegung(""))

