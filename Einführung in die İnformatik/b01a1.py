
#Gehalt
gehalt = 100000
prim = 2000
aufrittNetto=0
buroArbeitNetto=0


aufritt = int(input("Wie viele Auftritte hat Herr furby_datei.csv gemacht?: "))

if aufritt>4:
    aufrittNetto=(aufritt-4)* 400 + 4*300
else:
    aufrittNetto=4*300
buroArbeit=int(input("Wie viele Stunden Büroarbeit hat Herr furby_datei.csv gemacht?: "))
buroArbeitNetto=buroArbeit*100


print("\nGrundgehalt:",gehalt)
print("Prämie:", prim)
print("Einnahmen aus Auftritten:", aufrittNetto)
print("Einnahmen aus Büroarbeit:",buroArbeitNetto)
sum1=int(gehalt+prim+aufrittNetto+buroArbeitNetto)
print("Gesamteinkommen", str(sum1))
