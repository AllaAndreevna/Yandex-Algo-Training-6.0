# from collections import deque
#
# n, H = map(int, input().split())
# h = list(map(int, input().split()))
# w = list(map(int, input().split()))
# queue = deque()
# min1, min2 = -1, -1
# h_diff = []
#
# if w[0] < H:
#     queue.append(w[0])
# current_width = w[0]
# minimum_uncomf = float('inf')
#
# for i in range(1, n):
#     if current_width < H:
#         queue.append(w[i])
#         current_width += w[i]
#         diff = abs(h[i] - h[i - 1])
#         if h_diff and diff <= h_diff[-1][0]:
#             h_diff.append([diff, i])
#         elif not h_diff:
#             h_diff.append([diff, i])
#
#     else:
#         diff = abs(h[i] - h[i - 1])
#         minimum_uncomf = min(minimum_uncomf, h_diff[-1][0])
#         if diff == h_diff[-1][0] and queue[0] == w[h_diff[-1][1]]:
#             if h_diff[-1][1] != 1:
#                 h_diff.pop()
#             queue.popleft()
#         else:
#             current_width -= queue[0]
#             queue.popleft()
#     print(queue)
#     print(h_diff)
# print(minimum_uncomf)

from collections import deque

def min_discomfort(n, H, heights, widths):
    chairs = sorted(zip(heights, widths))
    height_que = deque()
    width_que = deque()
    height_diffs = deque()
    l = 0
    r = 1
    current_width = chairs[0][1]
    min_discomfort = float('inf')
    height_que.append(chairs[0][0])
    width_que.append(chairs[0][1])
    if width_que[0] == H:
        return 0
    if n == 1:
        return 0
    while r < n and l < n:
        height_que.append(chairs[r][0])
        width_que.append(chairs[r][1])
        if width_que[-1] == H:
            return 0
        if len(height_que) > 1:
            diff = abs(height_que[-1] - height_que[-2])
            while height_diffs and height_diffs[-1] < diff:
                height_diffs.pop()
            height_diffs.append(diff)
        else:
            return 0

        current_width += chairs[r][1]
        # print(height_diffs, l, r)
        while current_width >= H:
            if not height_diffs:
                return 0
            min_discomfort = min(min_discomfort, height_diffs[0])

            current_width -= chairs[l][1]
            if abs(height_que[1] - height_que[0]) == height_diffs[0]:
                height_diffs.popleft()
            if height_que:
                height_que.popleft()
                width_que.popleft()
            l += 1
        r += 1

    return min_discomfort



n, H = map(int, input().split())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))

result = min_discomfort(n, H, heights, widths)
print(result)
