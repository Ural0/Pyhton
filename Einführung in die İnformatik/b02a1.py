
#die anzahl der echten Teilern
n=int(input("Geben Sie Bitte eine Zahl: "))
sum=0
for i in range(2,n): # ausser 1 und n sich selbst
    if n%i==0:
        sum+=1
        print(i,end=", ")
print()
print(f"die anzahl der echten Teiler von: {n} sind:",sum)


