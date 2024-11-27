def check_if_postfix(s):
    stack = []
    operands = {"*", "+", "-"}
    for elem in s:
        try:
            val = int(elem)
            stack.append(val)
        except:
            if elem in operands:
                if elem == "*":
                    try:
                        result = stack[-1] * stack[-2]
                    except:
                        return "WRONG"
                elif elem == "+":
                    try:
                        result = stack[-1] + stack[-2]
                    except:
                        return "WRONG"
                elif elem == "-":
                    try:
                        result = stack[-2] - stack[-1]
                    except:
                        return "WRONG"
                stack.pop()
                stack.pop()
                stack.append(result)
        # print(stack)
    if len(stack) == 1:
        return stack[0]
    # print(stack)
    return "WRONG"


def check_if_infix(s):
    stack = []
    result_string = []
    operands = {"*", "+", "-"}
    i = 0
    while i < len(s):
        elem = s[i]
        if elem.isdigit():
            num_str = elem
            while i + 1 < len(s) and s[i + 1].isdigit():
                i += 1
                num_str += s[i]
            result_string.append(num_str)
        elif elem == "(":
            stack.append(elem)
        elif elem == ")":
            while stack and stack[-1] != "(":
                result_string.append(stack.pop())
            if not stack or stack[-1] != "(":
                return "WRONG"
            stack.pop()
        elif elem in operands:
            while (stack and stack[-1] in operands and
                   (elem == "+" or elem == "-" or (elem == "*" and stack[-1] == "*"))):
                result_string.append(stack.pop())
            stack.append(elem)
        i += 1
        # print(stack)
    if stack and stack[-1] == "(":
        return "WRONG"
    while stack:
        result_string.append(stack.pop())
    # print(result_string)

    return check_if_postfix(result_string)

def solve(s):
    ans1 = check_if_infix(s)
    ans2 = check_if_postfix(s)
    # print(ans1, ans2)
    if ans1 != "WRONG" and ans2 != "WRONG" and ans1 != ans2:
        return ans2
    elif ans1 != "WRONG" and ans2 == "WRONG":
        return ans1
    elif ans1 == "WRONG" and ans2 != "WRONG":
        return ans2
    elif ans1 == ans2 and ans1 != "WRONG":
        return ans1
    return "WRONG"

s = input()
print(solve(s))



