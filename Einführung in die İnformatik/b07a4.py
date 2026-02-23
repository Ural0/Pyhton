

def update_tree(baum, ebene=1):

    if type(baum) == int:
        return baum

    links, wurzel, recht = baum

    # Aktualisiere zuerst die Unterbaeume.
    neu_links = update_tree(links, ebene + 1)
    neu_recht = update_tree(recht, ebene + 1)

    #  Wenn beide Nachfolger int sind → aktualisiere
    if type(neu_links) == int and type(neu_recht ) == int:
        neu_wurzel = (neu_links + neu_recht ) * ebene
    else:
        neu_wurzel = wurzel

    return (neu_links, neu_wurzel,neu_recht)


baum=((111,-16,-26),81,-7) #

print(update_tree(baum)) # ((111, 170, -26), 81, -7) muss sein


