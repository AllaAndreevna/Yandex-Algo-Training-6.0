def solution(n, distance, monuments):
    correctMonuments = 0
    r = 0
    for l in range(n):
        while monuments[r] - monuments[l] <= distance and r < n - 1:
            r += 1
        if monuments[r] - monuments[l] > distance:
            correctMonuments += n - r
    return correctMonuments

n, r = map(int, input().split())
monuments = list(map(int, input().split()))
answer = solution(n, r, monuments)
print(answer)
