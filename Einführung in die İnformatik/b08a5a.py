
#bo8a6
def muenz_wechsel(betrag, min_muenze):
    muenzen = [1, 2, 5, 10, 20, 50, 100, 200]

    def hilfe(betrag, max_muenze):
        if betrag == 0:
            return [[]]
        if betrag < 0:
            return []

        ergebniss = []
        for m in muenzen:
            if min_muenze <= m <= max_muenze:
                for rest in hilfe(betrag - m, m):
                    ergebniss.append([m] + rest)
        return ergebniss

    zahlen = hilfe(betrag, max(muenzen))

    ausgabe = []
    for kombi in zahlen:
        neu = []
        for m in kombi:
            if m < 100:
                neu.append(f"{m} Cent")
            else:
                neu.append(f"{m//100} Euro")
        ausgabe.append(neu)

    return ausgabe


# Hauptprogramm
betrag = int(input("Geben Sie einen Betrag in Cent ein: "))
min_muenze = int(input("Geben Sie die kleinste Münze ein (in Cent): "))
out = muenz_wechsel(betrag, min_muenze)
for liste in out:
    print(liste)
