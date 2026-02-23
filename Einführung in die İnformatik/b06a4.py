
def enthaelt(l: list, element) -> bool:
    if l == []:
        return False
    if l[0] == element: #Wenn das erste Listenelement dem gesuchten Element entspricht
            return True
    return enthaelt(l[1:], element) # rekursiv im Rest der Liste weitersuchen


print(enthaelt([2, "b", 9, 2],"b"), "== True")
print(enthaelt([2, [1], [2]],[1]), "== True")

print(enthaelt([2, "ab", 9],"a"), "== False")
print(enthaelt([1, [[1]],[1, [1]]],[1]), "== False")
