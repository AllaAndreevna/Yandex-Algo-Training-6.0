def solve(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            stack.append(s[i])
        elif (s[i] == ")" or s[i] == "}" or s[i] == "]") and i == 0:
            return "no"
        elif s[i] == ")":
            if len(stack) > 0:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return "no"
            else:
                return "no"
        elif s[i] == "]":
            if len(stack) > 0:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return "no"
            else:
                return "no"
        elif s[i] == "}":
            if len(stack) > 0:
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return "no"
            else:
                return "no"

    if len(stack) == 0:
        return "yes"
    return "no"

s = input()
print(solve(s))
