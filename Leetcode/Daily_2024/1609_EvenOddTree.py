# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=1609. Even Odd Tree-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 28 - 2024
# URL: https://leetcode.com/problems/even-odd-tree
# ====================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        curr_level = 0

        if root.val %2 == 0:
            return False

        queue = deque()

        queue.append(root)

        while queue:
            
            if curr_level % 2 == 1:
                auxiliar = -float("inf")
            else:
                auxiliar = float("inf")

            for i in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    left_child = node.left.val
     
                    if curr_level % 2 == 1:
                        if auxiliar < left_child and left_child % 2 == 1:
                            auxiliar = left_child
                        else:
                            return False
                    else:
                        # 0
                        if auxiliar > left_child and left_child % 2 == 0:
                            
                            auxiliar = left_child
                        else:
                            return False


                if node.right:
                    queue.append(node.right)
                    right_child = node.right.val
                    print(auxiliar, right_child)
                    if curr_level % 2 == 1:
                        if auxiliar < right_child and right_child % 2 == 1:
                            auxiliar = right_child
                        else:
                            return False
                    else:
                        
                        if auxiliar > right_child and right_child % 2 == 0:
                            auxiliar = right_child
                        else:
                            return False


            
            curr_level += 1


        return True


