def search(root, key):
    current = root
    while current is not None:
        if key == current['key']:
            return True
        elif key < current['key']:
            current = current['left']
        else:
            current = current['right']
    return False

def insert(root, key):
    if root is None:
        return {'key': key, 'left': None, 'right': None}
    if key == root['key']:
        return root
    elif key < root['key']:
        root['left'] = insert(root['left'], key)
    else:
        root['right'] = insert(root['right'], key)
    return root

def find_min(node):
    while node['left'] is not None:
        node = node['left']
    return node

def delete(root, key):
    if root is None:
        return None
    if key < root['key']:
        root['left'] = delete(root['left'], key)
    elif key > root['key']:
        root['right'] = delete(root['right'], key)
    else:
        if root['left'] is None:
            return root['right']
        if root['right'] is None:
            return root['left']
        min_right = find_min(root['right'])
        root['key'] = min_right['key']
        root['right'] = delete(root['right'], min_right['key'])
    return root

def next_node(root, key):
    current = root
    succ = None
    while current is not None:
        if current['key'] > key:
            succ = current
            current = current['left']
        else:
            current = current['right']
    return succ

def previous_node(root, key):
    current = root
    pred = None
    while current is not None:
        if current['key'] < key:
            pred = current
            current = current['right']
        else:
            current = current['left']
    return pred


root = None

import sys

for line in sys.stdin:
    if not line.strip():
        continue
    parts = line.strip().split()
    cmd = parts[0]
    x = int(parts[1])

    if cmd == 'insert':
        root = insert(root, x)
    elif cmd == 'delete':
        root = delete(root, x)
    elif cmd == 'exists':
        print('true' if search(root, x) else 'false')
    elif cmd == 'next':
        node = next_node(root, x)
        print(node['key'] if node else 'none')
    elif cmd == 'prev':
        node = previous_node(root, x)
        print(node['key'] if node else 'none')
