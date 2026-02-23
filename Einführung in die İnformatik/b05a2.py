

def preimage(funktion, startintervall,zielintervall):

        i, j = startintervall # (-2,2) i=-2 & j=2
        #print(i,"--",j)
        a, b = zielintervall # (-2,2) a=-2 & b=2

        start = list(range(i, j + 1)) # range(-2,3)= [-2,-1,0,1,2]
        # print(start)
        ziel = list(range(a, b + 1)) # range(-2,3)= [-2,-1,0,1,2]
        result = []

        for y in ziel:
            liste = []
            for x in start:
                #print(x,"--",y)
                # liste.append((x,y))
                if funktion(x) == y:
                    liste.append(x)
            result.append(liste)

        return result

def g(zahl):
    return zahl + 1

def h(zahl):
    return 1

print(preimage(g,(-2,2 ),(-2,2)))
print(preimage(g,(6,10),(9,13)))
print(preimage(h,(12,14),(0,3)))
print(preimage(h,(12,14 ),(3,2)))

