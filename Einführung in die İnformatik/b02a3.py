
#"0" →True "00" →False "100" →True "-100" →True "--100" →False "01" →False "abc" →False "-01" →False " 10 " →False "-0" →True "1-0" →False "-00" →False
n=input("Geben einen String ein: ")
antwort = True


for i in range(0, len(n)):
    # 1. Gibt es eine Lücke?
    if n[i] == ' ':
        #print("Es beginnt mit einer Lücke.-- False")
        antwort = False
        break

    # 2. Wenn es mit „-“ beginnt (nur am Anfang prüfen)
    elif i == 0 and n[i] == "-":
        #print("mit „-“ beginnt")
        # Prüfe ob zweites Zeichen auch "-" ist
        if len(n) > 1 and n[1] == "-":
            #print("mit „--“ beginnt")
            antwort = False
            break
        # Prüfe ob nach "-" nur Zahlen kommen
        elif len(n) > 1 and  n[1:]  in "123456789":
            #print("Nach - kommen keine Zahlen")
            antwort = False
            break
        # Prüfe "-0" oder "-01" Fälle
        elif len(n) > 1 and n[1] == '0' and len(n) > 2:
            #print("Führende Null nach -")
            antwort = False
            break
        # Nur "-" alleine
        elif len(n) == 1:
            #print("Nur - alleine")
            antwort = False
            break

    # 3. Führende Null (nicht nach "-")
    elif i == 0 and n[0] == '0' and len(n) > 1:
        #print("Führende Null")
        antwort = False
        break

    # 4. Ungültige Zeichen (außer "-" am Anfang)
    elif i > 0 and n[i] not in "0123456789":
        #print("Ungültiges Zeichen:", n[i])
        antwort = False
        break

# Ergebnis ausgeben
print("-->", antwort)

