from typing import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def check_sum(self, node : TreeNode, target) -> bool:
        if not node: return False

        new_target = target - node.val

        if not node.left and not node.right:
            if new_target == 0: return True
            else: return False

        else:
            if self.check_sum(node.left, new_target) or self.check_sum(node.right, new_target):
                return True
            else:
                return False

    def hasPathSum(self, root : Optional[TreeNode], targetSum : int) -> bool:
        return self.check_sum(root, targetSum)
    

# a = TreeNode(7)
# b = TreeNode(2)
# c = TreeNode(11, a, b)
# d = TreeNode(1)
# e = TreeNode(4, left = None, right = d)
# f = TreeNode(13)
# g = TreeNode(8, f, e)
# h = TreeNode(4, left = c, right = None)
# z = TreeNode(5, left = h, right = g)

#print(Solution().hasPathSum(z, 22))

a = TreeNode(-3)
b = TreeNode(-2, left = None, right = a)

print(Solution().hasPathSum(b, -5))