import sys

n = int(input())
values = list(map(int, input().split()))

values.sort()

tree = []

def build_bst(array):
    if not array:
        return -1
    middle = len(array) // 2
    value = array[middle]
    left = build_bst(array[:middle])
    right = build_bst(array[middle+1:])
    tree.append([value, left, right])
    return len(tree) - 1 

root_idx = build_bst(values)

new_index = {}
order = []

def renumber(idx):
    if idx == -1:
        return -1
    new_index[idx] = len(order) + 1
    order.append(idx)
    return new_index[idx]

def dfs(idx):
    if idx == -1:
        return
    dfs(tree[idx][1])  
    dfs(tree[idx][2])  
    renumber(idx)

dfs(root_idx)

new_index = {}
order = []

def renumber_preorder(idx):
    if idx == -1:
        return -1
    new_index[idx] = len(order) + 1
    order.append(idx)
    renumber_preorder(tree[idx][1])
    renumber_preorder(tree[idx][2])

renumber_preorder(root_idx)

print(len(tree))
for idx in order:
    value, left, right = tree[idx]
    nl = new_index[left] if left != -1 else -1
    nr = new_index[right] if right != -1 else -1
    print(value, nl, nr)
print(1)
