

def kleinste_hoehe(x):
    # Base Case: negativ oder null sein → ungültig
    if x <= 0:
            return float("inf")

    # beide Regeln anwenden
    h1 = kleinste_hoehe(x - 34)
    h2 = kleinste_hoehe((x - 11) / 2)

    # Wenn beide Regeln ungültig sind -> dann ist x bereits das kleinste Element.
    if h1 == float("inf") and h2 == float("inf"):
        return x

    # den kleinsten Wert zurückgeben
    return min(h1, h2)

print(kleinste_hoehe(34.5))