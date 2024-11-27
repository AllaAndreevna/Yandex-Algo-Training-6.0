def solution(a, b, c, d):
    if (a == 0 and a == b and b == c and c == d) or (a == 0 and b == 0) or (c == 0 and d == 0):
        return 0, 0
    elif a == b and b == c and c == d:
        return a + 1, 1
    elif a == d == 0 or b == c == 0:
        return 0, 0
    elif a == 0 and b != 0:
        return 1, c + 1
    elif a != 0 and b == 0:
        return 1, d + 1
    elif c == 0 and d != 0:
        return a + 1, 1
    elif d == 0 and c != 0:
        return b + 1, 1
    m1 = a + 1
    n1 = c + 1
    m2 = b + 1
    n2 = d + 1
    if max(m1, m2) + 1 < min(m1 + n1, m2 + n2) and max(m1, m2) + 1 < max(n1, n2) + 1:
        return max(m1, m2), 1
    elif max(n1, n2) + 1 < min(m1 + n1, m2 + n2):
        return 1, max(n1, n2)
    elif m1 + n1 <= m2 + n2:
        return m1, n1
    else:
        return m2, n2

a = int(input())
b = int(input())
c = int(input())
d = int(input())
m, n = solution(a, b, c, d)
print(m, n)