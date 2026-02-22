#unterstring

# kendim yazamam bu kodu. Ezberlemem lazım. taki kafama oturuncaya kadar.

def f(s:str):
    #print(s)
    if s=="":
        return [""]
    substrings= f(s[1:])
    return substrings + [s[0] + sub for sub in substrings]


print(f("Cafe"))
print(f("abc"))
