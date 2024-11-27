def crop_diode_area(board):
    n = len(board)
    m = len(board[0]) if n > 0 else 0
    min_x, max_x = m, -1
    min_y, max_y = n, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == '#':
                min_x = min(min_x, j)
                max_x = max(max_x, j)
                min_y = min(min_y, i)
                max_y = max(max_y, i)
    if max_x == -1:
        return []
    cropped_board = []
    for i in range(min_y, max_y + 1):
        cropped_board.append(board[i][min_x:max_x + 1])
    return cropped_board

def is_rectangle_properly_defined(grid, min_x, min_y, max_x, max_y, fill_char):
    if min_x < 0 or min_y < 0 or max_x >= len(grid[0]) or max_y >= len(grid):
        return False
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if grid[y][x] != fill_char:
                return False
    return True

def find_bounds_on(board):
    n = len(board)
    m = len(board[0]) if n > 0 else 0
    min_x, max_x = m, -1
    min_y, max_y = n, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == '#':
                min_x = min(min_x, j)
                max_x = max(max_x, j)
                min_y = min(min_y, i)
                max_y = max(max_y, i)
    return (min_x, min_y, max_x, max_y)

def find_bounds_off(board):
    n = len(board)
    m = len(board[0]) if n > 0 else 0
    min_x_off = m
    max_x_off = -1
    min_y_off = n
    max_y_off = -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                min_x_off = min(min_x_off, j)
                max_x_off = max(max_x_off, j)
                min_y_off = min(min_y_off, i)
                max_y_off = max(max_y_off, i)
    return (min_x_off, min_y_off, max_x_off, max_y_off)

def check_I(board, min_x, min_y, max_x, max_y):
    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if board[i][j] != '#':
                return False
    return True

def check_O(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
    # Проверяем, что выключенный прямоугольник находится внутри включенного
    return (min_x < min_x_off <= max_x_off < max_x) and (min_y < min_y_off <= max_y_off < max_y) and \
           is_rectangle_properly_defined(board, min_x_off, min_y_off, max_x_off, max_y_off, ".")

def check_C(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
    # Проверяем, что выключенный прямоугольник находится строго внутри включенного
    return (min_x < min_x_off <= max_x_off <= max_x) and (min_y < min_y_off <= max_y_off < max_y) and \
           (max_x_off - min_x_off) < (max_x - min_x) and (max_y_off - min_y_off) < (max_y - min_y) and \
           is_rectangle_properly_defined(board, min_x_off, min_y_off, max_x_off, max_y_off, ".")


def check_L(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
    # Проверяем, что верхний правый угол выключенного совпадает с верхним правым углом включенного
    return (min_x < min_x_off and min_x_off <= max_x_off and max_x_off == max_x) and (min_y_off == min_y and max_y_off < max_y) and \
            is_rectangle_properly_defined(board, min_x_off, min_y_off, max_x_off, max_y_off, ".")

def check_H(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
    x5, y5 = -1, -1
    x6, y6 = -1, -1
    x3, y3 = -1, -1
    x4, y4 = -1, -1
    first_rectangle_found, second_rectangle_found = False, False
    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if board[i][j] == "." and not first_rectangle_found and not second_rectangle_found:
                x5, y6 = j, i
                x6 = x5
                y5 = y6
                first_rectangle_found = True
            elif j > 0 and i < max_y and board[i][j] == "#" and board[i][j - 1] == "." and board[i + 1][j - 1] == "#" and first_rectangle_found and (not second_rectangle_found):
                    x6 = j - 1
            elif i < max_y_off - 1:
                if board[i][j] == "#" and board[i - 1][j] == "." and first_rectangle_found and not second_rectangle_found:
                    y5 = i - 1
            elif first_rectangle_found and (not second_rectangle_found):
                if board[i][j] == ".":
                    x3, y4 = j, i
                    second_rectangle_found = True
    y3 = max_y_off
    x4 = max_x_off
    height = abs(min_y - max_y)
    # проверка неравенствами из условия
    if (min_x < x3 and x3 == x5 and x5 <= x4 and x4 == x6 and x6 < max_x) and \
            (height - min_y == y3 and y3 >= y4 and y4 > y5 and y5 >= y6 and y6 == height - max_y) and \
            (is_rectangle_properly_defined(board, x5, y6, x6, y5, ".")) and \
            (is_rectangle_properly_defined(board, x3, y4, x4, y3, ".")) and \
            (is_rectangle_properly_defined(board, min_x, min_y, x3 - 1, max_y, "#")):
        return True
    return False

def check_P(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
    x5, y5 = -1, -1
    x6, y6 = -1, -1
    x3, y3 = -1, -1
    x4, y4 = -1, -1
    first_rectangle_found, second_rectangle_found = False, False
    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if board[i][j] == "." and not first_rectangle_found and (not second_rectangle_found):
                x5, y6 = j, i
                x6 = x5
                y5 = y6
                first_rectangle_found = True
            elif j > 0 and i < max_y and board[i][j] == "#" and board[i][j - 1] == "." and board[i + 1][j - 1] == "#" and first_rectangle_found and (not second_rectangle_found):
                    x6 = j - 1
            elif i < max_y - 1:
                if board[i][j] == "#" and board[i - 1][j] == "." and first_rectangle_found and not second_rectangle_found:
                    y5 = i - 1
            elif first_rectangle_found and (not second_rectangle_found):
                if board[i][j] == "." and first_rectangle_found and (not second_rectangle_found):
                    x3, y4 = j, i
                    second_rectangle_found = True
    y3 = max_y
    x4 = max_x
    height = abs(min_y - max_y)
    # проверка неравенствами из условия
    if (min_x < x3 and x3 == x5 and x5 <= x6 and x6 < x4 and x4 == max_x) and \
            (height - min_y == y3 and y3 >= y4 and y4 > y5 and y5 >= y6 and y6 > height - max_y) and \
            (is_rectangle_properly_defined(board, x5, y6, x6, y5, ".")) and \
            (is_rectangle_properly_defined(board, x3, y4, x4, y3, ".")):
        return True
    return False


n = int(input())
board_input = [input().strip() for _ in range(n)]
board = crop_diode_area(board_input)
min_x, min_y, max_x, max_y = find_bounds_on(board)
min_x_off, min_y_off, max_x_off, max_y_off = find_bounds_off(board)
if max_x == -1:
    print('X')
else:
    if check_I(board, min_x, min_y, max_x, max_y):
        print('I')
    elif check_O(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
        print('O')
    elif check_C(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
        print('C')
    elif check_L(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
        print('L')
    elif check_H(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
        print('H')
    elif check_P(board, min_x, min_y, max_x, max_y, min_x_off, min_y_off, max_x_off, max_y_off):
        print('P')
    else:
        print('X')
