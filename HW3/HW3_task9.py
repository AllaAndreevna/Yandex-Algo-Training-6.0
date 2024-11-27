# from collections import deque
#
# N = int(input())
# a, b = map(int, input().split())
# rovers = []
#
# for i in range(N):
#     d, t = map(int, input().split())
#     rovers.append((d, t, i))
#
# rovers.sort(key=lambda x: x[1])
#
# print(rovers)
# queue1 = deque()
# queue2 = deque()
# queue3 = deque()
# queue4 = deque()
# result = [0] * N
# current_time = 1
# i = 0
# while i < N:
#     while rovers[i][1] == current_time:
#         if rovers[i][0] == 1:
#             queue1.append(rovers[i])
#         elif rovers[i][0] == 2:
#             queue2.append(rovers[i])
#         elif rovers[i][0] == 3:
#             queue3.append(rovers[i])
#         elif rovers[i][0] == 4:
#             queue4.append(rovers[i])
#         i += 1
#     print(queue1)
#     print(queue2)
#     print(queue3)
#     print(queue4)
#     print(i, current_time)
#     if queue1 and (queue1[0][0] == a or queue1[0][0] == b):
#         result[queue1[0][2]] = current_time
#         queue1.popleft()
#     if queue2 and (queue2[0][0] == a or queue2[0][0] == b):
#         result[queue2[0][2]] = current_time
#         queue2.popleft()
#     if queue3 and (queue3[0][0] == a or queue3[0][0] == b):
#         result[queue3[0][2]] = current_time
#         queue3.popleft()
#     if queue4 and (queue4[0][0] == a or queue4[0][0] == b):
#         result[queue4[0][2]] = current_time
#         queue4.popleft()
#
#     current_time += 1
#     print(result)
#     print(queue1)
#     print(queue2)
#     print(queue3)
#     print(queue4)
#
#
#     if queue1 and queue1[0][0] != a and queue1[0][0] != b:
#         if queue4 and queue4[0][0] != a and queue4[0][0] != b:
#             while queue4:
#                 result[queue4[0][2]] = current_time
#                 queue4.popleft()
#                 current_time += 1
#
#         result[queue1[0][2]] = current_time
#         queue1.popleft()
#
#
#     if queue2 and queue2[0][0] != a and queue2[0][0] != b:
#         if queue1 and queue1[0][0] != a and queue1[0][0] != b:
#             while queue1:
#                 result[queue1[0][2]] = current_time
#                 queue1.popleft()
#                 current_time += 1
#
#         result[queue2[0][2]] = current_time
#         queue2.popleft()
#
#     if queue3 and queue3[0][0] != a and queue3[0][0] != b:
#         if queue2 and queue2[0][0] != a and queue2[0][0] != b:
#             while queue2:
#                 result[queue2[0][2]] = current_time
#                 queue2.popleft()
#                 current_time += 1
#
#         result[queue3[0][2]] = current_time
#         queue3.popleft()
#
#     if queue4 and queue4[0][0] != a and queue4[0][0] != b:
#         if queue3 and queue3[0][0] != a and queue3[0][0] != b:
#             while queue3:
#                 result[queue3[0][2]] = current_time
#                 queue3.popleft()
#
#         result[queue4[0][2]] = current_time
#         queue4.popleft()
#
#
#     current_time += 1
#
#
#
#
# print(*result)



from collections import deque

N = int(input())
a, b = map(int, input().split())
rovers = []

for i in range(N):
    d, t = map(int, input().split())
    rovers.append((d, t, i))

rovers.sort(key=lambda x: x[1])

queues = {1: deque(), 2: deque(), 3: deque(), 4: deque()}
result = [0] * N
current_time = 1
i = 0

while i < N or any(queue for queue in queues.values()):
    while i < N and rovers[i][1] == current_time:
        queues[rovers[i][0]].append(rovers[i])
        i += 1

    can_pass = []

    for direction in [a, b]:
        if queues[direction]:
            can_pass.append(queues[direction][0])

    if can_pass:
        if len(can_pass) == 2:
            d1 = can_pass[0][0]
            d2 = can_pass[1][0]

            if (d1 == 1 and d2 == 2):
                result[can_pass[0][2]] = current_time
                queues[can_pass[0][0]].popleft()
            elif (d1 == 2 and d2 == 1):
                result[can_pass[1][2]] = current_time
                queues[can_pass[1][0]].popleft()
            elif (d1 == 2 and d2 == 3):
                result[can_pass[0][2]] = current_time
                queues[can_pass[0][0]].popleft()
            elif (d1 == 3 and d2 == 2):
                result[can_pass[1][2]] = current_time
                queues[can_pass[1][0]].popleft()
            elif (d1 == 3 and d2 == 4):
                result[can_pass[0][2]] = current_time
                queues[can_pass[0][0]].popleft()
            elif (d1 == 4 and d2 == 3):
                result[can_pass[1][2]] = current_time
                queues[can_pass[1][0]].popleft()
            elif (d1 == 4 and d2 == 1):
                result[can_pass[0][2]] = current_time
                queues[can_pass[0][0]].popleft()
            elif (d1 == 1 and d2 == 4):
                result[can_pass[1][2]] = current_time
                queues[can_pass[1][0]].popleft()
            else:
                for rover in can_pass:
                    result[rover[2]] = current_time
                    queues[rover[0]].popleft()
        else:
            for rover in can_pass:
                result[rover[2]] = current_time
                queues[rover[0]].popleft()

        current_time += 1
        continue
    secondary_pass = []
    for direction in range(1, 5):
        if direction not in [a, b]:
            if queues[direction]:
                secondary_pass.append(queues[direction][0])
    if secondary_pass:
        if len(secondary_pass) == 2:
            d1 = secondary_pass[0][0]
            d2 = secondary_pass[1][0]
            if (d1 == 1 and d2 == 2):
                result[secondary_pass[0][2]] = current_time
                queues[secondary_pass[0][0]].popleft()
            elif (d1 == 2 and d2 == 1):
                result[secondary_pass[1][2]] = current_time
                queues[secondary_pass[1][0]].popleft()
            elif (d1 == 2 and d2 == 3):
                result[secondary_pass[0][2]] = current_time
                queues[secondary_pass[0][0]].popleft()
            elif (d1 == 3 and d2 == 2):
                result[secondary_pass[1][2]] = current_time
                queues[secondary_pass[1][0]].popleft()
            elif (d1 == 3 and d2 == 4):
                result[secondary_pass[0][2]] = current_time
                queues[secondary_pass[0][0]].popleft()
            elif (d1 == 4 and d2 == 3):
                result[secondary_pass[1][2]] = current_time
                queues[secondary_pass[1][0]].popleft()
            elif (d1 == 4 and d2 == 1):
                result[secondary_pass[0][2]] = current_time
                queues[secondary_pass[0][0]].popleft()
            elif (d1 == 1 and d2 == 4):
                result[secondary_pass[1][2]] = current_time
                queues[secondary_pass[1][0]].popleft()
            else:
                for rover in secondary_pass:
                    result[rover[2]] = current_time
                    queues[rover[0]].popleft()
        else:
            for rover in secondary_pass:
                result[rover[2]] = current_time
                queues[rover[0]].popleft()

        current_time += 1
        continue

    current_time += 1

for ans in result:
    print(ans)