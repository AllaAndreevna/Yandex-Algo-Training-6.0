import sys

sys.setrecursionlimit(100000)

def calculate_height(node):
    if node in heights:
        return heights[node]

    if node == root:
        heights[node] = 0
    else:
        parent_height = calculate_height(tree[node])
        heights[node] = parent_height + 1
    return heights[node]

def find_LCA(u, v):
    while heights[u] != heights[v]:
        if heights[u] > heights[v]:
            u = tree[u]
        else:
            v = tree[v]
    while u != v:
        u = tree[u]
        v = tree[v]
    return u


n = int(input())
tree = {}
heights = {}
for _ in range(n - 1):
    child, parent = map(str, input().split())
    tree[child] = parent
root = (set(tree.values()) - set(tree.keys())).pop()
while True:
    try:
        u, v = map(str, input().split())
        calculate_height(u)
        calculate_height(v)
        LCA = find_LCA(u, v)
        print(LCA)
    except:
        break