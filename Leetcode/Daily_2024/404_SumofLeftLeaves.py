# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 404. Sum of Left Leaves-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: April- 13 - 2024
# URL: https://leetcode.com/problems/sum-of-left-leaves/
# ====================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def auxiliar(root, isLeft):
            if not root:
                return 0

            if not root.left and not root.right and isLeft:
                return root.val

            
            return auxiliar(root.left, True) + auxiliar(root.right, False)

        return auxiliar(root.left, True) + auxiliar(root.right, False)
        