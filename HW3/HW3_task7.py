from collections import deque

n, b = map(int, input().split())
a = list(map(int, input().split()))
que = deque()
ans = 0
for i in range(n):
    que.extend([i] * a[i])
    len_que = len(que)
    ans += len_que
    if len_que <= b:
        for popping in range(len_que):
            que.popleft()
    else:
        for popping in range(b):
            que.popleft()
    # print(que)
    # print(ans)

if que:
    ans += len(que)
print(ans)
#
#
#
# n, b = map(int, input().split())
# a = list(map(int, input().split()))
#
# total_wait_time = 0
# current_queue = 0
#
# for i in range(n):
#     current_queue += a[i]
#     total_wait_time += current_queue
#     if current_queue > b:
#         current_queue -= b
#     else:
#         current_queue = 0
#
# total_wait_time += current_queue
#
# print(total_wait_time)
