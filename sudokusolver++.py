def uygun_mu(matrix, satir, sutun, sayi_degeri):

    if sayi_degeri in matrix[satir]:
        return False


    if sayi_degeri in [matrix[i][sutun] for i in range(9)]:
        return False


    yeni_satir = (satir // 3) * 3
    yeni_sutun = (sutun // 3) * 3
    for i in range(3):
        for j in range(3):
            if matrix[yeni_satir + i][yeni_sutun + j] == sayi_degeri:
                return False

    return True


def solver(matrix, satir=0, sutun=0):

    if sutun == 9:
        satir += 1
        sutun = 0
        if satir == 9:
            return True


    if matrix[satir][sutun] > 0:
        return solver(matrix, satir, sutun + 1)


    for sayi_degeri in range(1, 10):
        if uygun_mu(matrix, satir, sutun, sayi_degeri):
            matrix[satir][sutun] = sayi_degeri


            if solver(matrix, satir, sutun + 1):
                return True

            matrix[satir][sutun] = 0 

    return False


if __name__ == "__main__":
    sudoku = [
        [1, 0, 7, 0, 3, 0, 0, 0, 0],
        [0, 8, 3, 0, 1, 6, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 7, 0, 3],
        [2, 0, 4, 0, 3, 9, 0, 0, 6],
        [5, 0, 7, 0, 0, 0, 0, 0, 0],
        [8, 0, 6, 0, 0, 7, 1, 0, 0],
        [0, 7, 1, 6, 2, 5, 3, 0, 4],
        [4, 6, 2, 3, 8, 1, 9, 5, 0],
        [0, 0, 8, 9, 7, 4, 2, 0, 1]
    ]

    if solver(sudoku):
        for row in sudoku:
            print(" ".join(map(str, row)))
    else:
        print("Bu sudoku yanlıştır, çözülemez")
    