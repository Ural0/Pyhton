

#b11a1
from copy import deepcopy


def det(M: list[list[int]]) -> int:
    x1, x2, x3 = M[0]
    x4, x5, x6 = M[1]
    x7, x8, x9 = M[2]
    return x1 * (x5 * x9 - x6 * x8) - x2 * (x4 * x9 - x6 * x7) + x3 * (x4 * x8 - x5 * x7)



def show(m):
    # jeder Spalte lange
    widths = []
    for col in range(len(m[0])):
        max_width = 0
        for row in range(len(m)):
            max_width = max(max_width, len(str(m[row][col])))
        widths.append(max_width)

    # matrisi
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]:<{widths[j]}}", end=" ")
        print()

    print()  # Leerzeile



def zero_determinant(entries: list[int]) -> None:
    current = []

    def backtrack():
        if len(current) == 9:
            M = [
                current[0:3],
                current[3:6],
                current[6:9]
            ]
            if det(M) == 0:
                show(M)
            return

        for x in entries:
            current.append(x)
            backtrack()
            current.pop()

    backtrack()



M = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
N=[[12,2,3],[4,514,6],[7,85,9]]
z=[0, 1]

print(det(M))
print()
show(N)
zero_determinant(z)


