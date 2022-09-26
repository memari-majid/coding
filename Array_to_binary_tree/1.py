'''
Array to Binary Tree
'''



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_BT(nums):
    def helper(left, right):
        if left > right:
            return None
        p = (left + right) // 2
        print(p)
        root = TreeNode(nums[p])
        root.left = helper(left, p - 1)
        root.right = helper(p + 1, right)
        return root

    return helper(0, len(nums) - 1)



nums = [0, 1, 2, 3, 4, 5]
result = array_to_BT(nums)
