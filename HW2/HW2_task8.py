def min_transitions(n, a):
    pref = [0] * (n + 1)
    suff = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i - 1]
    for i in range(n - 1, -1, -1):
        suff[i] = suff[i + 1] + a[i]
    min_move = 0
    for i in range(1, n):
        min_move += a[i] * i
    left_sum = 0
    right_sum = min_move
    for osp in range(1, n):
        left_sum += pref[osp]
        right_sum -= suff[osp]
        min_move = min(min_move, left_sum + right_sum)
    return min_move



n = int(input())
a = list(map(int, input().split()))
print(min_transitions(n, a))
