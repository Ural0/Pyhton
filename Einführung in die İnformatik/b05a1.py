


def csv_nach_zeilentupel(dateipfad) -> list:
    x =open(dateipfad,'r').readlines()
    #print("x Inhalt = ",x)
    liste = []
    for zeile in x:
        zeile = zeile.strip() # \n und Leerzeichen löschen
        teile=zeile.split(',') # trennen
        teile = [t.strip() for t in teile] # auch alle anderen Teile entfernen
        liste.append(tuple(teile)) # Tupel bilden

    return liste


def aufraeumen(datenbank):

    neu_list=[]
    for tup in datenbank:
        name=tup[0]  # Bsp: 'Pink Flamingo'
        tail=tup[3]  # Bsp: 'Tail'

        zahlen=list(tup[4:]) # Nimm die Zahlenkolonnen (beginnend mit dem 4. Index).
        zahlen=zahlen[::-1] #die Zahlen umkehren(absteigend)
        #print(zahlen)

        # Neues Tupel erstellen
        ne_tuple=(name,tail)+tuple(zahlen)
        neu_list.append(ne_tuple)
    return neu_list

def ident(aufgeraumte):
    # 1. Liste alphabetisch sortieren (nach dem ersten Element)
    sortierte_lsit=sorted(aufgeraumte,key=lambda x: x[0].lower())

    new_liste=[]
    # 2. ID hinzufügen (beginnend mit 1)
    for i, tup in enumerate(sortierte_lsit, start=1):
        new_liste.append((str(i),) + tup) # <- ID als string
    return new_liste


def arithm_mittel(einkommen) -> tuple:

    neu_list=[]
    for zeile in einkommen:
        #print(zeile[3:]) # Die Zahlen zeigen 3. Nach dem Index

        # Die ersten drei Elemente bleiben als String. (ID, Name, Tail)
        feste_Teil=zeile[:3]

        zahlen=[]
        # Die Übrigen: Bestandszahlen (string -> int)
        summme=0
        for s in zeile[3:]:
            zahlen.append(int(s))
            summme+=int(s)

        # Arithmetischer Mittelwert
        # mittel_wert=sum(zahlen)/len(zahlen)
        mittel_wert = summme/ len(zahlen)

        # Neues Tupel erstellen
        neus_Tuple=feste_Teil + tuple(zahlen) + (mittel_wert,)
        neu_list.append(neus_Tuple)

    #print("arithmeik  ", neu_list)
    return neu_list


def median(datenbank):
        tail_mittel = []
        mane_mittel = []

        # 1. Durchschnitte trennen
        for tup in datenbank:
            accessoire = tup[2]  # 'Tail' oder 'Mane'
            mittel = tup[-1]  # letztes Element -> arithmetischer Mittelwert

            if accessoire == 'Tail':
                tail_mittel.append(mittel)
            else:
                mane_mittel.append(mittel)

        # 2. Mini-Funktion zur Berechnung des Medians
        def berechne_median(liste):
            liste.sort()
            n = len(liste)

            if n % 2 == 1:
                return liste[n // 2]
            else:
                return (liste[n // 2 - 1] + liste[n // 2]) / 2

        # 3. Berechne die Mediane
        tail_med = berechne_median(tail_mittel)
        mane_med = berechne_median(mane_mittel)

        # 4. Auf Konsole drucken
        print("Tail:", tail_med)
        print("Mane:", mane_med)

        return None


#Datei Weg
dateipfad = r"/Users/ural/Desktop/furby_datei.csv"  # für Mcbook


print("csv_nach_zeilentupel: ",csv_nach_zeilentupel(dateipfad))
print("aufraeumen:",aufraeumen(csv_nach_zeilentupel(dateipfad)))
print("ident: ",ident(aufraeumen(csv_nach_zeilentupel(dateipfad))))
print("Arithmetik Mittel: ",arithm_mittel(ident(aufraeumen(csv_nach_zeilentupel(dateipfad)))))
print(median(arithm_mittel(ident(aufraeumen(csv_nach_zeilentupel(dateipfad))))))
