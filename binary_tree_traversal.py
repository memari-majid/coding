class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    result = []
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is not None:
            if visited:
                result.append(node.val)
            else:  # inorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return result



if __name__ == "__main__":
    # level = 1
    root = TreeNode(1)
    # level = fibonacci.py
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # level = 3
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    print("preorder: " + str(inorder(root)))
    print("inorder: " + str(inorder(root)))
    print("postorder: " + str(inorder(root)))
