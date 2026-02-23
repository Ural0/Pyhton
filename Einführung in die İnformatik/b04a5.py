
#Hausaufgabe 4 A5
def anwenden(L, bedingung, f, g):
    newListe=[]
    for e in L:
        if bedingung(e)==True:
            newListe.append(f(e))
        else:
            newListe.append(g(e))
    print(newListe)

# vorher gegebene Funktionen als Beispiel
def ist_warm(temp):
    return temp >= 25
def erhohe(temp):
    return temp+1
def verdoppele(temp):
    return temp * 2

#unsere eigene Funktionen
def ist_Minus(x):
    return x < 0
def verdreifache(y):
    return y*3
def halbiere(h):
    return h / 2

#print("Original Liste:[24.0, 25.0, 26.5]")
anwenden([24.0, 25.0, 26.5], ist_warm, erhohe, verdoppele)

#anwenden([-4.0, 8, 3], ist_Minus, verdreifache, halbiere)

