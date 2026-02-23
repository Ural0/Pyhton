

def filter(Liste: list, bedingung):

    if Liste==[]:
        return Liste
    if bedingung(Liste[0])==True:
        return [Liste[0]] + filter(Liste[1:],bedingung)
    return filter(Liste[1:],bedingung)


def test_bed(zahl):
    return zahl < 10


print(filter([19,-2,10,9], test_bed), "== [-2,9]")
