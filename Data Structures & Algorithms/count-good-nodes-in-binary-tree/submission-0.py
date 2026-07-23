# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, max): 
            print(root.val)
            if root.left is None and root.right is None and root.val >= max: 
                return 1 

            new_max = max 
            x = 0 
            if root.val >= max: 
                new_max = root.val 
                x = 1 
            l, r = 0, 0
            if root.left is not None: 
                l = helper(root.left, new_max)
            if root.right is not None: 
                r = helper(root.right, new_max) 
            return x + r + l
            

        return helper(root, -100)