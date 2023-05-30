
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 100. Same Tree  -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: May - 30 - 2023
# URL: https://leetcode.com/problems/same-tree/description/
# ====================================================================

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_arr = []
        self.preOrder(p,p_arr)

        q_arr = []
        self.preOrder(q,q_arr)
        return p_arr == q_arr

    

    def preOrder(self, root, array):
        if not root:
            array.append("Null")
            return None
        
        array.append(root.val)
        self.preOrder(root.left,array)
        self.preOrder(root.right, array)

