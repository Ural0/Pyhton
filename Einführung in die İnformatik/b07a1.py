
def int_superliste(n: list):

    if n == []:
        return True

    erstes = n[0]
    if type(erstes)== list:
         # Zuerst muss die Unterliste selbst eine Superliste sein.
         if not int_superliste(erstes):
             return False
         # Wenn das naechste Element int ist,: wieder gemischter Typ => False
         if len(n) > 1 and isinstance(n[1], int):
             return False
         return int_superliste(n[1:])

    elif type(erstes) == int:
        if len(n) > 1 and type(n[1])== list:
            return False
        return int_superliste(n[1:])
    else:
        return False

def klonen(lis):
    if type(lis) == int:
        return lis

    neu_liste=[]
    for element in lis:
        neu_liste.append(klonen(element))
    return neu_liste


print(int_superliste([1,2,3]))
print(int_superliste([1,[1],3]))
#print(int_superliste([[1,2],[[1],[3,4]],[3]]))
#print(int_superliste([[1,2],[[1],[3,4]],3]))


#print(klonen([1,2,3]))
#print(klonen([1,[1],3]))
#print(klonen([[1,2],[[1],[3,4]],[3]]))

