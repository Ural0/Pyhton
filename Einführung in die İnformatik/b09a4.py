# Abgabegruppe 18
# Mehmet Emin Ural = 35923466
# Anita Feyzi      = 36416255
# Iram Iram        = 36266942

#b09a4
def print_combo(wort):
    count=0

    while wort[0]==" " or wort[-1]==" ":
        print("1. ") # Wenn am Anfang oder am Ende ein Leerzeichen steht, wird dieser Code ausgeführt.
        if wort[0]==" ":
            print("2. ") # Wenn am Anfang ein Leerzeichen eingegeben wird, werden die Zeichen nach dem Leerzeichen als Wort genommen
            wort=wort[1:]
        elif wort[-1]==" ": # Wenn am Ende ein Leerzeichen eingegeben wird, wird dieses Leerzeichen gelöscht und das verbleibende Wort wird als das eigentliche Wort genommen.
            print("3. ")
            wort=wort[:-1]

    while wort!="":
        print("4.while ") # Wenn am Anfang oder am Ende des Wortes keine Leerzeichen vorhanden sind, wird dieser Teil direkt ausgeführt.
        for j in range(1,len(wort)):
            print("5.for ")
            count+=1 #
            print(wort[0]+wort[j]) # Das Wort wird vom 0. Index und allen nachfolgenden Zeichen ausgegeben.
        wort=wort[1:] # Der 0. Index wird entfernt und das Wort beginnt mit dem nächsten Zeichen.

ein=input("Bitte Eingabe tätigen: ")
print_combo(ein)

# Leerzeichen = IndexError: string index out of range Fehler wird ausgegeben.
# Einzelner Buchstabe wird nicht ausgegeben - mit einem Buchstaben und Leerzeichen funktioniert es.


