
def uygun_mu(matrix, satir, sutun, sayi_degeri):


    for sayi in range(9):
        if matrix[satir][sayi] == sayi_degeri:
            return False

    for sayi in range(9):
        if matrix[sayi][sutun] == sayi_degeri:
            return False


    yeni_satir = satir - satir % 3
    yeni_sutun = sutun - sutun % 3
    for i in range(3):
        for j in range(3):
            if matrix[yeni_satir + i][yeni_sutun + j] == sayi_degeri:
                return False

    return True


def solver(matrix, satir = 0, sutun = 0):
    if sutun == 9:
        satir += 1
        sutun = 0
        if satir == 9:
            return True

    if matrix[satir][sutun] > 0:
        return solver(matrix, satir, sutun + 1)

    for sayi_degeri in range(1,10):
        if uygun_mu(matrix, satir, sutun, sayi_degeri):
            matrix[satir][sutun] = sayi_degeri

            if solver(matrix, satir, sutun + 1):
                return True

        matrix[satir][sutun] = 0

    return False




if __name__ == "__main__":
    sudoku = [
        [2, 0, 4, 0, 6, 1, 0, 0, 9],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 6, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    if solver(sudoku):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=' ')
            print("")
    else:
        print("Bu sudoku yanlıştır, çözülemez")