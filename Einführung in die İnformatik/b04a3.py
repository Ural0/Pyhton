

#H 4 A3
def parse_Daten(daten):
   # print("Getrennt: ", daten.split(";"))
    new=[]
    for x in daten.split(";"):
        name,noten=x.split(",")
        #print(name,"-",noten)
        new.append((name,float(noten)))
    return print(new)




parse_Daten("Alfons,2.3;Ben,3.0;Carla,1.7")





