
#OOB
class Studi:
    def __init__(self,matrikelnummer:str, nachname: str, L:list[float]):
        self.matrikelnummer = matrikelnummer
        self.nachname = nachname
        self.L = sorted(L)

    def average(self):
        #notendurchnistt
        return sum(self.L)/len(self.L)

    def add_note(self,note:float):

      if not(1<=note<=6):
         # raise "ValueError"
         raise ValueError("ValueError")
         print("ValueError")
      else:
        self.L.append(note)
        self.L=sorted(self.L)

    """ 
    try:
        if 1<=note <=6:
          self.L.append(note)
    except ValueError:
        print("ValueError")
    """



a1= Studi(1,"Max",[9,6,5])
print(a1.matrikelnummer,a1.nachname,a1.L)
print("Average= ",a1.average())
print("add_note",a1.add_note(3))
#print("add_note",a1.add_note(99))
print(a1.L)