import sys


def transpose(matrix):
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            sys.stdout.write(str(matrix[x][y]) + " ")
        sys.stdout.write("\n")
        sys.stdout.flush()


macierz = [[1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
transpose(macierz)
