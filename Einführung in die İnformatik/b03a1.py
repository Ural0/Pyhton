

import random

def zufallsstring(A, laenge):
    zufalls_laenge = random.choice(range(0, laenge ))  # Zufaellige Laenge auswaehlen

    ergebnis = ""
    for i in range(zufalls_laenge):  # waehle in jeder Position einen zufälligen Buchstaben aus.
        ergebnis += random.choice(A)
    # senden
    return ergebnis

#vorher gegebene Code
def wort_bzgl_laenge(n, A, l):
    ergebnis = ""
    for i in range(l - 1, -1, -1):  # i in {l-1,...,0} der Exponent vom MSB zum LSB
        ergebnis += A[n // len(A) ** i]
        n = n % len(A) ** i
    return ergebnis

#vorher gegebene Code
def wort(n, A):
    l = 0
    b = len(A)
    while n >= b ** l:
        n = n - b ** l
        l += 1
    return wort_bzgl_laenge(n, A, l)


def alphpos(a, A):
    #eine Zeichenfolge und ein Buchstabe wird gesucht. Die Position dieses Buchstabens innerhalb dieser Zeichenfolge
    for i in range(len(A)):
        if a == A[i]:
            # print(i)
            return i
    else:
        return -1


def lexpos(s, A):
    basis = len(A)  #Anzahl der Zeichen im Alphabet furby_datei.csv
    n = 0 # n=Hier wird am Ende die lexikographische Position stehen
    for ch in s:  # für jeden Buchstaben (ch)
        n = n * basis + alphpos(ch, A) #einem Stellenwertsystem = n * basis + aktuellen Zeichens im Alphabet
    return n


def laengenlexpos(s, A):
    n = len(A)
    l = len(s)

    # kurze Wörter zaehlen. Anzahl aller Wörter, die kürzer sind als s
    kurze = 0
    for i in range(l):
        kurze += n ** i       #Es gibt n**i Wörter der Laenge i

    #  + seinen Platz in seiner Gruppe finden
    return kurze + lexpos(s, A) #Position von s innerhalb der Gruppe aller Wörter der Laenge l


def trans(s, A, B):
    return wort(laengenlexpos(s, A), B)
    # nimmt die Position von s im Alphabet furby_datei.csv und erzeugt das Wort an genau derselben Position im Alphabet B

#vorher gegebene Code
def kleiner(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) < laengenlexpos(Z, A)

#vorher gegebene Code
def groesser(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) > laengenlexpos(Z, A)

#vorher gegebene Code
def gleich(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) == laengenlexpos(Z, A)


def suche_z_linear(alphabet):
    global vergleichszaehler, maxPasswortLaenge

    # Versuche alle Laengen von 0 bis maxPasswortLaenge.von 0 bis zur maximal erlaubten Passwortlaenge.
    for laenge in range(0, maxPasswortLaenge + 1):
        anzahl_woerter = len(A) ** laenge
        for pos in range(anzahl_woerter):
            w = wort_bzgl_laenge(pos, A, laenge) # Erzeuge das Wort an der Position 'pos' # innerhalb der Wörter genau dieser Länge
            if gleich(w, A):
                return w #gefunden, gebe Wort zurück


def suche_z_binaer(alphabet, laenge):
    global vergleichszaehler

    # Suchbereich festlegen
    left = 0
    right = 0

    for i in range(1, laenge + 1):
        right += len(A) ** i

    right = right - 1

    while left <= right:
        mid = (left + right) // 2 # Mitte berechnen
        w = wort(mid, A) # Wort an Position mid im lexikographischen Wörterbuch erzeugen

        if gleich(w, A):
            return w
        elif kleiner(w, A):
            left = mid + 1
        else:
            right = mid - 1

    return None

#vorher gegebene Code
if __name__ == "__main__":
    ag = int(input("Geben Sie eine Alphabetgröße zwischen 1 und 26 ein: "))
    maxPasswortLaenge = int(input("Geben Sie die maximale Passwortlänge ein: "))
    suchArt = int(input("Soll lineare Suche [0], binäre Suche [1] oder beides [2] angewendet werden? "))
    A = ""
    for i in range(ord("furby_datei.csv"), ord("furby_datei.csv") + ag):
        A = A + chr(i)
    Z = zufallsstring(A, maxPasswortLaenge)
    print("zufaellig erzeugter String: ", Z)
    if suchArt == 0 or suchArt == 2:
        vergleichszaehler = 0
        g = suche_z_linear(A)
        print(g + " gefunden mit linearer Suche")
        print("Test war" + (" erfolgreich" if g == Z else " erfolglos"))
        print(str(vergleichszaehler) + " Vergleiche wurden verwendet")  # zu hoch? siehe Notizen
    if suchArt == 1 or suchArt == 2:
        vergleichszaehler = 0
        g = suche_z_binaer(A, maxPasswortLaenge)
        print(g + " gefunden mit binärer Suche")
        print("Test war" + (" erfolgreich" if g == Z else " erfolglos"))
        print(str(vergleichszaehler) + " Vergleiche wurden verwendet")