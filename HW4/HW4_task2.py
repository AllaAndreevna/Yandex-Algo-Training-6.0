import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

n = int(input())

A = defaultdict(list)
children = set()
parents = set()

for _ in range(n - 1):
    child, parent = input().strip().split()
    A[parent].append(child)
    children.add(child)
    parents.add(parent)

root = (parents - children).pop()

descendants = {name: 0 for name in parents.union(children)}

# print(A)
def calculate_descendants(name):
    if name in descendants and descendants[name] != 0:
        return descendants[name]

    total_descendants = 0
    for child in A[name]:
        total_descendants += calculate_descendants(child) + 1  # добавить предков child + 1 для самого этого ребенка
    descendants[name] = total_descendants
    # memo[name] = total_descendants
    return total_descendants

calculate_descendants(root)

output = sorted(descendants.items())

for key, val in output:
    print(key, val)