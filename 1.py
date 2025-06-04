n = int(input())

if n == 0:
    print("YES")
    exit()

nodes = []
for i in range(n):
    x, left, right = map(int, input().split())
    left = left - 1 if left != -1 else -1
    right = right - 1 if right != -1 else -1
    nodes.append((x, left, right))

root = int(input()) - 1

def is_bst(index, min_value, max_value):
    if index == -1:
        return True

    value, left, right = nodes[index]

    if not (min_value < value < max_value):
        return False

    return is_bst(left, min_value, value) and is_bst(right, value, max_value)

if is_bst(root, float('-infinity'), float('infinity')):
    print("YES")
else:
    print("NO")
