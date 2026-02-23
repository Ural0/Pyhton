
def woerter(k, l):
    alphabet = [str(i) for i in range(k)]
    print(alphabet)
    ergebnis = []

    def backtrack(wort):
        print("CALL  ->", wort)
        if len(wort) == l:          # Abbruchbedingung
            print("SAVE==  ->", wort)
            ergebnis.append(wort)
            return
        for zeichen in alphabet:   # Möglichkeiten
            print("TRY   ->", wort, "+", zeichen)
            backtrack(wort + zeichen)

            #Her backtrack çağrısı kendi for’unu başlatır

    backtrack("")
    return ergebnis

print(woerter(2,4))
