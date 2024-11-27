class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search(root, x):
    if root is None:
        return False
    if root.value == x:
        return True
    if x < root.value:
        return search(root.left, x)
    return search(root.right, x)

def add(root, x):
    if root is None:
        return Node(x)
    if x < root.value:
        root.left = add(root.left, x)
    elif x > root.value:
        root.right = add(root.right, x)
    return root

def printtree(root, depth=0):
    if root is not None:
        printtree(root.left, depth + 1)
        print('.' * depth + str(root.value))
        printtree(root.right, depth + 1)

tree = None
# ключ - родитель, значения - его 2 ребенка. но классом удобнее
root = None

while True:
    try:
        string = input().split()
        if string[0] == "ADD":
            x = int(string[1])
            if search(root, x):
                print("ALREADY")
            else:
                tree = add(root, x)
                root = tree
                print("DONE")
        elif string[0] == "SEARCH":
            x = int(string[1])
            if tree is not None and search(root, x):
                print("YES")
            else:
                print("NO")
        elif string[0] == "PRINTTREE":
            printtree(root)
    except:
        break