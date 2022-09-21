# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive(root):
    if root is None:
        return 0
    else:
        left_height = recursive(root.left)
        right_height = recursive(root.right)
        return max(left_height, right_height) + 1


def iterative(root):
    stack = []
    depth = 0
    if root:
        stack = [(root, 1)]
    while stack:
        (node, current_depth) = stack.pop(-1)
        if node is not None:
            depth = max(depth, current_depth)
            stack.append((node.left,current_depth+1))
            stack.append((node.right,current_depth+1))
    return depth
    


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

print(recursive(root))
print(iterative(root))

