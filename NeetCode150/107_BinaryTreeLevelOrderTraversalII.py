# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=- 107. Binary Tree Level Order Traversal II -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Meduium
# 
# Date: November - 29 - 2023
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii
# ====================================================================

# First Approach - Recursive
# Time Complexity : O(n)
# Space Complexity: O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        traversal_nodes = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            level = []
            
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)

            traversal_nodes.append(level)

        return traversal_nodes[::-1]