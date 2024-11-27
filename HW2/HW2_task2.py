def CountPrefSums(n, nums):
    prefsum = [0] * (n + 1)
    nowsum = 0
    for now in range(1, n + 1):
        nowsum += now
        prefsum[now] = prefsum[now - 1] + nums[now - 1]
    return prefsum
def CountKNums(k, prefsum):
    cnt = 0
    prevval = dict()
    for nowsum in prefsum:
        if nowsum - k in prevval:
            cnt += prevval[nowsum - k]
        if nowsum not in prevval:
            prevval[nowsum] = 0
        prevval[nowsum] += 1
    return cnt



n, k = map(int, input().split())
cars = list(map(int, input().split()))
prefsum = CountPrefSums(n, cars)
answer = CountKNums(k, prefsum)
print(answer)
