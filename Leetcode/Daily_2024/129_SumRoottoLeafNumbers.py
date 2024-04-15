# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 129. Sum Root to Leaf Numbers-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: April - 14- 2024
# URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# ====================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, number):
            if not root:
                return 0

            if not root.left and not root.right:
                return int(number + str(root.val))

            return dfs(root.left, number + str(root.val)) + dfs(root.right, number + str(root.val))


        return dfs(root, '')
