class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    stack = []
    # once in the beginning
    if root != None:
        stack.append((1,root))

    depth = 0
    while stack:
        current_depth,root = stack.pop()
        # each time traverse to new node
        if root != None:
            # don't count None depth
            depth = max(current_depth, depth)
            # first left
            stack.append((current_depth+1,root.left))
            # second right
            stack.append((current_depth+1,root.right))
    return depth

def maxDepth(root):
    return 1 + max((maxDepth(root.left, maxDepth(root.right)))) if root else 0

if __name__ == '__main__':
    #   3
    #  /\
    # 9 20
    #   /\
    # 15 7
    root = Node(3, Node(9), Node(20, Node(15), Node(7)))
    print(maxDepth(root))
