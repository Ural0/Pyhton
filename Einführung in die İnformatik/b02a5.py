

saetze=input("Geben Sie eien Satze ein: ")
Zaehler=0
#max_Zaehler=0                                                                                                                                                                                                                                                                                                                                                                                       """                     ""                          """
anfang=0

for i in range(0, len(saetze)):
    if saetze[i]== ' ' or  i == len(saetze)-1:
        if saetze[i] == " ":
            ende = i
        else:
            ende = i + 1

        wort = saetze[anfang:ende]  # das Wort nehmen
        sayac = 0
        max_Zaehler = 0

        wort = saetze[anfang:ende]
        #print("Leerzeichen gefunden und gefundenes Wort=",wort)
        anfang = i + 1  #  der Anfang des nächsten Wortes

        for i in range(len(wort)):
            if wort[i] not in "aeiouAEIOU" :
                Zaehler= Zaehler + 1
                if Zaehler > max_Zaehler:
                    max_Zaehler = Zaehler

            else:
                Zaehler = 0
        print(wort, max_Zaehler)
        Zaehler = 0

    else:
        ende = i +1
        wort = saetze[anfang:ende]

#Technik macht Spass
