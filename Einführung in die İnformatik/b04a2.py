

#H 4 A2
import random

def lotto(anzahl : int, maximum : int):
    if 1 < anzahl and anzahl < maximum:
        zahlen = []
        random_zahlen=list(range(1, maximum))
        for i in range(anzahl):
            zufaelige_zahl = random.choice(random_zahlen)
            zahlen.append(zufaelige_zahl)
            random_zahlen.remove(zufaelige_zahl)  ## Jede Nummer darf nur einmal verwendet werden.

        zusattNummer=random.choice(random_zahlen)

    return (zahlen, zusattNummer)

print(lotto(6,49))