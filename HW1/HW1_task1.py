def solution(x1, y1, x2, y2, x, y):
    if x > x1 and x < x2:
        if abs(y - y2) < abs(y - y1):
            return "N"
        else:
            return "S"
    elif y > y1 and y < y2:
        if abs(x - x1) < abs(x - x2):
            return "W"
        else:
            return "E"
    else:
        if x <= x1 and y >= y2:
            return "NW"
        elif x <= x1 and y <= y1:
            return "SW"
        elif x >= x2 and y >= y2:
            return "NE"
        else:
            return "SE"

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())
print(solution(x1, y1, x2, y2, x, y))