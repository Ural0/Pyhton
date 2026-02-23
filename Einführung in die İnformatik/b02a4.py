

zeichenkette=input("Bitte geben Sie einen String: ")
zeichen=input("Zeichnen: ")

running=True
gefunden=False

while running:
    for i in range(0,len(zeichenkette)):
        if zeichenkette[i] == zeichen and gefunden==False:
            print("Die erste Position des Zeichens",zeichenkette[i], "ist",i)
            running = False
            gefunden = True
    if not gefunden:
        print(-1)
    running = False