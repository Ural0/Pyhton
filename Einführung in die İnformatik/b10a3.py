
#b10a3
def all_mod_sum(k, l) ->dict:
    return  {w: sum(int(x)for x in w) %k for w in words(k,l)}

def words(k, l):
    alphabet = [str(i) for i in range(k)]
    ergebnis = []

    def backtrack(wort):

        if len(wort) == l:  # abbruchbedingung
            ergebnis.append(wort)
            return
        for zeichen in alphabet: #alphabet=["0","1"] # Möglichkeiten
            backtrack(wort + zeichen)

    backtrack("")
    return ergebnis

print(all_mod_sum(2,5))
