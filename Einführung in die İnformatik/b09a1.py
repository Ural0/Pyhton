

#b09a1
def string_funk(s1, s2):
    assert len(s1) >= 3, "laenge muss mindestens 3 sein"
    assert len(s1) == len(s2) * 2, "s1 muss doppelt so lang wie s2 sein"
    assert s1[:3] == s2[:3], "die ersten Buchstaben passen nicht"
    return s1+s2

def nutzer_aufruf():
    s1=input("Geben Sie S1 ein: ")
    s2=input("Geben Sie S2 ein: ")

    try:
        ergebnis= string_funk(s1, s2)
        print(ergebnis)
    except AssertionError:
        print("Eingaben nicht zulässig.")


nutzer_aufruf()
