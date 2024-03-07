import random

def print_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(map(str, row)))

def is_valid_move(sudoku, row, col, num):
    # Satır kontrolü
    if num in sudoku[row]:
        return False

    # Sütun kontrolü
    if num in [sudoku[i][col] for i in range(9)]:
        return False

    # 3x3 bölge kontrolü
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

def generate_sudoku():
    # Boş bir Sudoku tahtası oluştur
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    # Sudoku tahtasını çöz
    solve_sudoku(sudoku)

    # Bazı sayıları tahtadan kaldır (soru olarak bırak)
    remove_count = random.randint(17, 25)  # Bu sayıyı ayarlayarak zorluk derecesini kontrol edebilirsiniz
    for _ in range(remove_count):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while sudoku[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        sudoku[row][col] = 0

    return sudoku

def solve_sudoku(sudoku):
    empty_location = find_empty_location(sudoku)

    if not empty_location:
        return True  # Sudoku tamamlandı

    row, col = empty_location

    for num in range(1, 10):
        if is_valid_move(sudoku, row, col, num):
            sudoku[row][col] = num

            if solve_sudoku(sudoku):
                return True  # Sudoku çözüldü

            sudoku[row][col] = 0  # Backtrack

    return False  # Sudoku çözülemez

def find_empty_location(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None

if __name__ == "__main__":
    generated_sudoku = generate_sudoku()

    print("Üretilen Sudoku Tahtası:")
    print_sudoku(generated_sudoku)
