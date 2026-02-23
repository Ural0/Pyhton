

#H4 A4
def haufigkeit(s):
    list = []
    verwendete = []
    for buchstabe in s:
        if buchstabe not in verwendete:
            zeahler = 0  # wird für jedes Buchstaben auf Null gesetzt
            for h in s:
                if h == buchstabe:  # Wenn es derselbe Buchstabe ist, wird der zeahler erhöht.
                    zeahler += 1
            list.append((buchstabe, zeahler))
            verwendete.append(buchstabe)
    return list


def ausgabe(haufigkeit_Rückgabe):
    print(haufigkeit_Rückgabe)
    summe=0
    for buchStabe,zahl in haufigkeit_Rückgabe:
        print(buchStabe,": ","*"*zahl) #Histogramm
        summe+=zahl
    print(summe)

ausgabe(haufigkeit("Hallo"))
