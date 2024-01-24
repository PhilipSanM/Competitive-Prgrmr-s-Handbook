# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1457. Pseudo-Palindromic Paths in a Binary Tree -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 24 - 2024
# URL: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# ====================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        counter = 0
        def dfs(root, path, repetitions, odds):
            if not root:
                return 

            nonlocal counter

            # check the leaf
            if not root.right and not root.left:
                path.append(root.val)
                repetitions[root.val] = repetitions.get(root.val, 0) + 1

                if repetitions[root.val] % 2 == 1:
                    odds.add(root.val)
                else:
                    odds.remove(root.val)

                if len(odds) <= 1:
                    counter += 1
                
                path.pop()
                repetitions[root.val] -= 1

                if repetitions[root.val] % 2 == 1:
                    odds.add(root.val)
                else:
                    odds.remove(root.val)


            path.append(root.val)

            repetitions[root.val] = repetitions.get(root.val, 0) + 1

            if repetitions[root.val] % 2 == 1:
                odds.add(root.val)
            else:
                odds.remove(root.val)


            dfs(root.left, path, repetitions, odds)
            dfs(root.right, path, repetitions, odds)


            path.pop()
            repetitions[root.val] -= 1

            if repetitions[root.val] % 2 == 1:
                odds.add(root.val)
            else:
                odds.remove(root.val)


        dfs(root, [], {}, set())


        return counter