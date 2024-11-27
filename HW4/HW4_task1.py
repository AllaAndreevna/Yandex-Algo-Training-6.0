n = int(input())

A = dict()
children = set()
parents = set()

for _ in range(n - 1):
    child, parent = input().strip().split()
    A[child] = parent
    children.add(child)
    parents.add(parent)

root = (parents - children).pop()

heights = {root: 0}

# print(A.items())
def calculate_heights(name, current_height):
    for child, parent in A.items():
        if parent == name:
            heights[child] = current_height + 1
            calculate_heights(child, current_height + 1)

calculate_heights(root, 0)

output = sorted(heights.items())

for key, val in output:
    print(key, val)