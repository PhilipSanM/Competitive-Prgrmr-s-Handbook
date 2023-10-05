# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-110. Balanced Binary Tree -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: October - 04- 2023
# URL: https://leetcode.com/problems/balanced-binary-tree/
# ====================================================================

# Using dfs
# Time Complexity : O(n)
# Space Complexity: O(1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
            
        def dfs( root):
            if not root:
                return [0, True]

            left = dfs( root.left)
            right = dfs( root.right)

            balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1

            return [1 + max(left[0], right[0]), balanced]

        sol = dfs( root)
        return sol[1]