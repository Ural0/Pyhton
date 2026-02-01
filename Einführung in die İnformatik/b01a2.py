
#Zahlrechner

running: bool = True
ergebnis: int=0
zahl: int =0
op = "+"
while running:
    x: str = input("")
    if x== "stop":

        #
        if op == "+":
            ergebnis += zahl
        elif op == "-":
            ergebnis -= zahl
        elif op == "*":
            ergebnis *= zahl
        running = False
        print("=", ergebnis)
    elif x in "0123456789" and len(x)==1 :
        #print("zahl: ",x)
        zahl=int(x)

    elif x == '+' or x == '-' or x == '*':

        if op== "+":
            ergebnis = ergebnis + zahl
        elif op == '-':
            ergebnis = ergebnis - zahl
        elif op == '*':
            ergebnis = ergebnis * zahl
        op = x
    else:
         print("invalid input")
         running = False
