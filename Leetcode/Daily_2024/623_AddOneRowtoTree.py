# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 623. Add One Row to Tree -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: April - 15 - 2023
# URL: https://leetcode.com/problems/add-one-row-to-tree/
# ====================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        def dfs(root, curr_depth):
            if not root:
                return

            if curr_depth == depth - 1:
                

                auxiliar_left = root.left
                auxiliar_right = root.right

                root.left = TreeNode(val)
                root.right = TreeNode(val)
                
                root.left.left = auxiliar_left
                root.right.right = auxiliar_right

            dfs(root.left, curr_depth + 1)
            dfs(root.right, curr_depth + 1)

        dfs(root, 1)

        return root




