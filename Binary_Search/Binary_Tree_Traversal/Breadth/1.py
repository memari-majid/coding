class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse(root):
    result = []
    if root is None:
        return result
    queue = []
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.pop(0)
            # add the node to the current level
            current_level.append(current_node.val)
            # insert the children of current node in the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)

    return result


def main():
    # level = 1
    root = TreeNode(1)
    # level = 2
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # level = 3
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Level order traversal: " + str(traverse(root)))


main()
