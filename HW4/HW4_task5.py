import sys

sys.setrecursionlimit(100000)
from collections import defaultdict

def search_subtree(tree, node, parent):
    # if x not in parent:
    #     return 1
    total_count = 1
    for child in tree[node]:
        if child != parent:
            count = search_subtree(tree, child, node)
            total_count += count
    count_subtree[node] = total_count
    return total_count


v = int(input())
tree = defaultdict(list)

# parents = set()
# children = set()
for _ in range(v - 1):
    parent, child = map(int, input().strip().split())
    tree[parent].append(child)
    tree[child].append(parent) # так как граф неориентированный
    # parents.add(parent)
    # children.add(child)

count_subtree = [0] * (v + 1)
search_subtree(tree, 1, -1)


# print(tree)
# print(count_subtree)

print(' '.join(map(str, count_subtree[1:])))