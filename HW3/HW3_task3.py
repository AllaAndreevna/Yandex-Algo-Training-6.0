from collections import deque

def min_sliding_window(nums, k):
    if not nums or k <= 0:
        return []
    result = []
    dq = deque()
    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] > nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

n, k = map(int, input().split())
ms = list(map(int, input().split()))

ans = min_sliding_window(ms, k)
for i in range(len(ans)):
    print(ans[i])