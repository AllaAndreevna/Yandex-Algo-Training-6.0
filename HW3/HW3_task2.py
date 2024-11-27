def solve(n, ms):
    stack = []
    answer = [-1] * n
    for i in range(n):
        if len(stack) == 0:
            stack.append([ms[i], i])
        else:
            if ms[i] >= stack[-1][0]:
                stack.append([ms[i], i])
            elif ms[i] < stack[-1][0]:
                while stack and stack[-1][0] > ms[i]:
                    answer[stack[-1][1]] = i
                    stack.pop()
                stack.append([ms[i], i])
    return " ".join(map(str, answer))

n = int(input())
ms = list(map(int, input().split()))
print(solve(n, ms))