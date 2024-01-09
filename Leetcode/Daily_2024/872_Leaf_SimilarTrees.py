# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 872. Leaf-Similar Trees -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: January - 9- 2023
# URL: https://leetcode.com/problems/leaf-similar-trees/
# ====================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        


        def dfs(root, sequence):
            if not root:
                return

            if not root.left and not root.right:
                sequence.append(root.val)
                return

            dfs(root.left, sequence)
            dfs(root.right, sequence)


        a = []
        b = []

        dfs(root1, a)
        dfs(root2, b)
        return a == b