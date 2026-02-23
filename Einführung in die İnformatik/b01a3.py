
#Streichhölzern

print("Mit wie vielen Streichhölzern soll gespielt werden?",end=" ")
ingesamt=int(input(""))
print("|"*ingesamt)

restlicheStreichhölzer=ingesamt
spieler=0

while int (restlicheStreichhölzer)>0:
    print("Spieler",spieler,"wie viele Streichholzer nimmst du weg?",end=" ")
    zahl=int(input(""))
    if zahl>3 or zahl<1:
        print("Sie sind disqualifiziert")
        restlicheStreichhölzer=0
    elif zahl<=restlicheStreichhölzer:
        restlicheStreichhölzer = (restlicheStreichhölzer - zahl)
        print("|" * int(restlicheStreichhölzer))
        if restlicheStreichhölzer==0:
                print("Spieler", 1-spieler," hat gewonnenn!")
    else:
        print( "Üngültiger Zug,Spieler ",spieler," ist disqualifiziert. Spieler ", 1-spieler,"hat gewonnen")

        restlicheStreichhölzer = 0
    spieler = 1 - spieler
