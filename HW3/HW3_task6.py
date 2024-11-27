n = int(input())
w = input()
s = input()

dic = {w[i]: i for i in range(4)}
min_opening = ""
for elem in dic:
    if elem == "[" or elem == "(":
        min_opening = elem
        break
stack = []
answer = list(s)
count_closed_pairs = 0
if len(s) == n:
    print(s)
else:
    for char in s:
        if char in "([":
            stack.append(char)
        else:
            if stack and ((char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[')):
                stack.pop()
                count_closed_pairs += 1


    # while count_closed_pairs * 2 + len(stack) * 2 < n:
    while len(answer) < n and count_closed_pairs * 2 + len(stack) * 2 < n:
        if stack and stack[-1] == "[":
            if dic["]"] <= dic[min_opening]:
                answer.append("]")
                stack.pop()
                count_closed_pairs += 1
            else:
                answer.append(min_opening)
                stack.append(min_opening)
        elif stack and stack[-1] == "(":
            if dic[")"] <= dic[min_opening]:
                answer.append(")")
                stack.pop()
                count_closed_pairs += 1
            else:
                answer.append(min_opening)
                stack.append(min_opening)
        # print(answer)
        elif len(stack) == 0:
            stack.append(min_opening)
            answer.append(min_opening)
    # print(min_opening)
    # print(answer)
    while len(answer) < n:
        if stack[-1] == "[":
            answer.append("]")
        else:
            answer.append(")")
        stack.pop()
    print(''.join(answer))