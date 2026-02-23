

def anfang_von(m,n):
    #print(m[0] , n[0])
    if len(m)==0 or len(n)==0:
     return True

    if m[0] == n[0]:# Wenn die ersten Elemente übereinstimmen, rekursiv weiter mit den Restlisten prüfen
        return anfang_von(m[1:],n[1:])
    return False


print(anfang_von((2,"b",9,100), (2,"b",9)),"== True")
print(anfang_von((2,"b",9), (2,"b",9,100)),"== True")
print(anfang_von((2,"b",9), (2,9)),"== False")