class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sym1(root):
    def mirror(l, r):
        if l and r and l.val == r.val:
            return mirror(l.left, r.right) and mirror(l.right, r.left)
        return l == r
    return not root or mirror(root.left, root.right)


def sym3(root: Node) -> bool:
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        l, r = stack.pop()
        if not l and not r:
            continue
        if not l or not r or (l.val != r.val):
            return False
        stack.append((l.left, r.right))
        stack.append((l.right, r.left))
    return True


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(3)
    root.right.left = Node(4)

    result = sym3(root)

