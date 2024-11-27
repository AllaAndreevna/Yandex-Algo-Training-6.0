def remove_medians(n, ms):
    a = sorted(ms)
    result = []
    if n % 2 == 0:
        left, right = (n // 2) - 1, n // 2
    else:
        left, right = n // 2, n // 2
        result.append(a[left])
        left -= 1
        right += 1
    while left > -1 and right < n + 1:
        result.append(a[left])
        left -= 1
        result.append(a[right])
        right += 1
    return result


n = int(input())
a = list(map(int, input().split()))
result = remove_medians(n, a)
print(" ".join(map(str, result)))