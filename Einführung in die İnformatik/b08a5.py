
#bo8a5
def muenz_wechsel(betrag, min_muenze):

    muenzen = [1, 2, 5, 10, 20, 50, 100, 200]
    memo = {}

    def hilfe(betrag, min_m, max_m):
        key = (betrag, min_m, max_m)
        if key in memo:
            return memo[key]

        if betrag == 0:
            return [[]]
        if betrag < 0:
            return []

        result = []

        for m in muenzen:
            if min_m <= m <= max_m:
                for rest in hilfe(betrag - m, min_m, m):
                    result.append([m] + rest)

        memo[key] = result
        return result

    zahlen = hilfe(betrag, min_muenze, max(muenzen))

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


betrag=int(input("Geben Sie einen Betrag in Cent ein: "))
min_munze=int(input("Geben Sie die kleinste Münze ein (in Cent): "))
out=muenz_wechsel(betrag,min_munze)
for liste in out:
    print(liste)