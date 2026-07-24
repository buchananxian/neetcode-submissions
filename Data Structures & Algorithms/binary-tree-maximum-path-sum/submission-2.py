# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def helper(root): 
            if root is None: 
                return -1001, -1001
            left1, left2 = helper(root.left) 
            right1, right2 = helper(root.right) 
            left1, right1 = max(left1, 0), max(right1, 0) 

            return root.val + max(left1, right1), max(left2, right2, root.val + left1 + right1) 

        return helper(root)[1] 