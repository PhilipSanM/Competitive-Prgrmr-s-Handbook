# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 104. Maximum Depth of Binary Tree -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: May - 28 - 2023
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# ====================================================================

# First Approach - Recursive
# Time Complexity : O(n)
# Space Complexity: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if not root:
            return depth
        
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        

# Post : https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/3572831/python-s-recursive-delight-the-easiest-solution-o-n/
