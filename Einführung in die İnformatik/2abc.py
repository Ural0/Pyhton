

#2a sorusu
def get_studie(matrikelNum: str, nachname:str, L: list):
    return (int(matrikelNum),str(nachname),[(L)])

def notenDurch(x):
    #print(sum(x[2]))
    #print(len(x[2]))
    return sum(x[2]) / len(x[2])

def betterListCompre(L: list,s):
    return [student for student in L if notenDurch(student) >notenDurch(s) ]

#2b
def better(L: list, s):
   # notVonS=s[2]

    new=[]
    for i in L:
        if sum(i[2]) / len(i[2])> sum(s[2]):
            new.append(i)
    return new

#2c
def best(L: list):
    print("Best")
    print(L)
    return min(L, key=lambda x:notenDurch(x))
   # return [student for student in L min(student)]

L = [("123", "x1", [1, 2, 3]),("456", "x2", [2, 2, 2]),("789", "X2", [13, 3, 3]) ]
S = ("789", "Demir", [5, 1, 1])


print(get_studie("030333","ural",[2,34]))

print(better(L,S))

print(notenDurch(S))

print(betterListCompre(L,S))

print(best(L))