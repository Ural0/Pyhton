import random

#b10a5
def rand_labyrinth():
    length = random.randint(1,23)
    out = []
    for step in range(length):
        out.append(random.choice(["R","L"]))
    return out

def solve_labyrinth():
    # Bakctracking
    L = loesung
    def backtracking(weg):
        if len(weg) >23:
            return None
        if weg !=L[:len(weg)]:
            return None
        if weg == L:
            return weg
        for schritt in ["R","L"]:
            rest= backtracking(weg + [schritt])

            if rest is not None:
                return rest

    return backtracking([])

loesung = rand_labyrinth()
print(loesung)
print(solve_labyrinth())





