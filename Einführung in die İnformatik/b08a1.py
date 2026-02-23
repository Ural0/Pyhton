
#bo8a
def umkehren(wb):

    #print(wb.keys())
    #print(wb.values())

    newWb={}
    for a,b in wb.items():
        #print(a,b) # a = key , b=value
        if b not in newWb:
            newWb[b]=a
        else:
            if a < newWb[b]:
                newWb[b] = a

    return newWb


print(umkehren({2:3, 4:"ab", 5:True, 9:"ab"}))
