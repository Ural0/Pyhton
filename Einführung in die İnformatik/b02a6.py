
#Matrix
hohe=int(input("Hohe: "))
breite=int(input("Breite: "))
print(hohe, "x", breite)

for i in range(0,hohe):
    for j in range(0,breite):
        if i==j:       # wenn indiz i==j gleich sind, dann schreibt 1 sonst 0
            print("1",end="")
        else:
            print("0",end="")
    print()