
def pyramide(n):
    # Hilfsfunktion: fügt links und rechts jeweils eine Spalte Leerzeichen hinzu
    def pyramide_padded(p):
        zeilen = p.split("\n")
        ergebnis = ""
        for z in zeilen:
            ergebnis += " " + z + " \n"
        return ergebnis.rstrip("\n")

    # Basisfall: Höhe 1 → eine einzelne Spitze
    if n == 1:
        return "*"
    else:
        # Rekursiver Aufbau: kleinere Pyramide + neue Basiszeile
        return pyramide_padded(pyramide(n - 1)) + "\n" + (2 * n - 1) * "*"


def pyramide_seq(n, k):
    # Basisfall 1 keine weitere Unterteilung
    if k == 0:
        return pyramide(n)

    # Basisfall 2 minimale Höhe
    if n == 1:
        return "*"

    # Rekursive Berechnung der linken und rechten Teilsequenz
    links = pyramide_seq(n // 2, k - 1)
    mitte = pyramide(n)
    rechts = pyramide_seq(n // 2, k - 1)

    # Aufteilen in einzelne Zeilen
    links_zeilen = links.split("\n")
    mitte_zeilen = mitte.split("\n")
    rechts_zeilen = rechts.split("\n")

    # Breiten der einzelnen Blöcke bestimmen
    breite_links = max(len(z) for z in links_zeilen)
    breite_mitte = max(len(z) for z in mitte_zeilen)
    breite_rechts = max(len(z) for z in rechts_zeilen)

    # Vertikale Ausrichtung Teilsequenzen unten ausrichten
    offset_links = len(mitte_zeilen) - len(links_zeilen)
    offset_rechts = len(mitte_zeilen) - len(rechts_zeilen)

    ergebnis = []

    # Zeilenweise Kombination links – mitte – rechts
    for i in range(len(mitte_zeilen)):
        # Linker Block
        if i < offset_links:
            l = " " * breite_links
        else:
            l = links_zeilen[i - offset_links].ljust(breite_links)

        # mittlerer Block
        m = mitte_zeilen[i].ljust(breite_mitte)

        # rechter Block
        if i < offset_rechts:
            r = " " * breite_rechts
        else:
            r = rechts_zeilen[i - offset_rechts].ljust(breite_rechts)

        ergebnis.append(l + " " + m + " " + r)

    return "\n".join(ergebnis)


print(pyramide_seq(5, 1))