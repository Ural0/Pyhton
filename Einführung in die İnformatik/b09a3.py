
#b09a3
def add_val(wb, s: str, i:int):

    if s in wb:
        print(wb[s])
        if i not in wb[s]:
            wb[s].append(i)
    else:
        print("Fehlermeldung ")
    print(wb) #In jedem Fall wird das, ggf. angepasste, Wörterbuch zurückgegeben.
    print()

wb={"x":[1,3,5],"y":[2,4,6],"z":[5,10,15]}

add_val(wb,"x",22) # nicht in drin
add_val(wb,"y",4) # in drin
add_val(wb,"d",7) # Schlüssel enthalt nicht