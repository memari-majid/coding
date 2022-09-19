'''
Array to Binary Tree
'''



class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_BT(nums):
    def helper(left, right):
        # break
        if left > right:
            return None
        # left middle
        p = (left + right) // 2
        # preorder
        root = Node(nums[p])
        root.left = helper(left, p - 1)
        root.right = helper(p + 1, right)
        return root

    return helper(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    result = array_to_BT(nums)
