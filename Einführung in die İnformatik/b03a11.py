

import random

def zufallsstring(A, laenge):
    zufalls_laenge = random.choice(range(0, laenge)) #Zufällige Länge auswählen
    # rastegle sayı önce seçiliyor

    ergebnis = ""
    #Sonra seçilen rastegel sayısıı kadar for döngüüs dönüyoır
    for i in range(zufalls_laenge): # waehle in jeder Position einen zufälligen Buchstaben aus.
        ergebnis += random.choice(A)

    # Ergebnis senden
    return ergebnis


def wort_bzgl_laenge(n, A, l):
    ergebnis = ""
    for i in range(l - 1, -1, -1):  # i in {l-1,...,0} der Exponent vom MSB zum LSB
        ergebnis += A[n // len(A) ** i]
        n = n % len(A) ** i
    return ergebnis

def wort(n, A):
    l = 0
    b = len(A)
    while n >= b ** l:
        n = n - b ** l
        l += 1
    return wort_bzgl_laenge(n, A, l)


#Es gibt eine Zeichenfolge und ein Buchstabe wird gesucht. Die Position dieses Buchstabens innerhalb dieser Zeichenfolge#
def alphpos(a, A):
    for i in range(len(A)):
        if a == A[i]:
            #print(i)
            return i
    else:
        return -1


def lexpos(s, A):
    basis = len(A)
    n = 0
    for ch in s:  # für jeden Buchstaben (ch)
        n = n * basis + alphpos(ch, A)
    return n


def laengenlexpos(s, A):
    n = len(A)
    l = len(s)

    # kurze Wörter zaehlen
    kurze = 0
    for i in range(l):
        kurze += n ** i

    #  seinen Platz in seiner Gruppe finden
    return kurze + lexpos(s, A)


def trans(s, A, B):
    return wort(laengenlexpos(s, A), B)


def kleiner(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) < laengenlexpos(Z, A)


def groesser(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) > laengenlexpos(Z, A)


def gleich(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) == laengenlexpos(Z, A)

"""
def suche_z_linear(alphabet):
    return ""

"""


def suche_z_binaer(A, max_laenge):
    global vergleichszaehler

    # Suchbereich festlegen
    left = 0
    #right = sum(len(furby_datei.csv) ** i for i in range(1, max_laenge + 1)) - 1 Aşaığıda bu kodu yapıyor
    right = 0

    for i in range(1, max_laenge + 1):
        right += len(A) ** i

    right = right - 1

    while left <= right:
        mid = (left + right) // 2
        w = wort(mid, A)

        if gleich(w, A):
            return w
        elif kleiner(w, A):
            left = mid + 1
        else:
            right = mid - 1

    return None

def suche_z_linear(A):
    global vergleichszaehler, maxPasswortLaenge

    # Versuche alle Laengen von 1 bis maxPasswortLaenge.
    for laenge in range(1, maxPasswortLaenge + 1):
        anzahl_woerter = len(A) ** laenge

        # Probiere jedes mögliche Wort dieser Laenge aus
        for pos in range(anzahl_woerter):
            w = wort_bzgl_laenge(pos, A, laenge)  # Erzeuge das Wort an der Position 'pos' # innerhalb der Wörter genau dieser Länge
            if gleich(w, A):
                return w
    #return None
    #return -1

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

