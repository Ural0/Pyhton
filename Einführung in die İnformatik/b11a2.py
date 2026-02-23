
#b11a2
from copy import deepcopy

# Schachbrett ausgeben
def show(B: list[list[str]]) -> None:
    for row in B:
        print(" ".join(row))
    print()   # Leerzeile


def initialize_board(n: int) -> list[list[str]]:# Leeres Schachbrett initialisieren
    return [["0"] * n for _ in range(n)]


def put_queen(B: list[list[str]], pos: tuple[int, int]) -> None:#  Dame setzen und bedrohte Felder markieren
    n = len(B)
    r, c = pos

    # Dame platzieren
    B[r][c] = "Q"

    # Zeile und Spalte
    for i in range(n):
        if B[r][i] == "0":
            B[r][i] = "X"
        if B[i][c] == "0":
            B[i][c] = "X"

    # Diagonalen
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        i, j = r + dr, c + dc
        while 0 <= i < n and 0 <= j < n:
            if B[i][j] == "0":
                B[i][j] = "X"
            i += dr
            j += dc



def free_fields(B: list[list[str]], row: int) -> list[int]:# Freie Felder ("0") in einer Zeile finden
    return [col for col in range(len(B)) if B[row][col] == "0"]



def n_queens(n: int) -> None: #  n-Damen-Problem lösen
    board = initialize_board(n)

    def backtrack(row: int, B: list[list[str]]) -> None:
        if row == n:
            show(B)
            return

        for col in free_fields(B, row):
            B_copy = deepcopy(B)
            put_queen(B_copy, (row, col))
            backtrack(row + 1, B_copy)

    backtrack(0, board)




# Bsp aufruf
n_queens(5)
