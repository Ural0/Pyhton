
#b10a4
def remove_A_a(s):
    return "".join(map(lambda i: i if i!="a" and i!="A" else "", s))


def remove_A_b(s):
    #mittels filter (ohne map zu benutzen). Nennen Sie diese Funktion remove_A_b.
    return "".join(filter(lambda i: i!="a" and i!="A", s))



print(remove_A_a("adak"))
print(remove_A_a("abcAac"))
print(remove_A_b("ahhmacAo"))

