def solution(n, k, ms):
    a = sorted(ms)
    left = 0
    max_count = 0
    for right in range(n):
        while a[right] - a[left] > k:
            left += 1
        max_count = max(max_count, right - left + 1)
    return max_count

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solution(n, k, a))