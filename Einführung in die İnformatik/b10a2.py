
#b10a2
def alph_dict(zahl):
  return {i+1: [chr(ord("a")+j) for j in range(i+1)][::-1] for i in range(0, zahl) }


print(alph_dict(5)) # zwischen 1 und 26

#{1:["a"], 2:["b","a"], 3:["c","b","a"], 4:["d","c","b","a"], 5:["e","d","c","b","a"], 6:["f","e","d","c","b","a"]}
