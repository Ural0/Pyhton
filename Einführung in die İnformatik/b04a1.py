
# 4 A1
def durschnitt(name, notenListe):
    summe=0
    for noten in notenListe:
        summe+=noten
    durchnit=summe/len(notenListe)

    #print("Name:", name, ", NotenListe", notenListe,", Summe der Noten: ", summe, "Notendurchnitt:", durchnit)
    return name,durchnit


liste = [
    ("Agathe", [2.3, 1.7, 1.3]),
    ("Ben", [3.0, 2.7]),
    ("Clara", [1.0, 1.3, 1.0, 1.3])
]
#print("Original Liste:", liste)

durchschnittsliste = []

for i ,y in liste:
    #print(i,"<--->", y)
    durchschnittsliste.append(durschnitt(i,y))


print(durchschnittsliste)