n = int(input())
stack = []
prefsum = [0]
for i in range(n):
    command = input()
    if command[0] == "+":
        val = int(command[1:])
        stack.append(val)
        if not prefsum:
            prefsum.append(val)
        else:
            new_val = prefsum[-1] + val
            prefsum.append(new_val)
    elif command[0] == "-":
        print(stack.pop())
        prefsum.pop()
    elif command[0] == "?":
        count_number = int(command[1:])
        print(prefsum[-1] - prefsum[-1 - count_number])
