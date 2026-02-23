
#bo8a3
def wort_paare(s):

    WB = {}
    worte=s.split()
    for i in range(len(worte)-1):
        #print(worte[i], worte[i+1])
        zwei_worter=worte[i], worte[i+1]
        if zwei_worter not in WB:
            WB[zwei_worter] = 1
        else:
            WB[zwei_worter] +=1

    return WB

wort_paare("der Hund lauft und der Hund lauft schnell und der Hund bellt")
