# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-2385. Amount of Time for Binary Tree to Be Infected -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 9- 2024
# URL: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
# ====================================================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        adjency_list = {}

        queue = deque()

        queue.append((root, 0))
    

        while queue:
            for i in range(len(queue)):
                data = queue.popleft()
                node = data[0]
                adjency_list[node.val] = []

                if node.left:
                    queue.append((node.left, node.val))
                    adjency_list[node.val].append(node.left.val)
                if node.right:
                    queue.append((node.right, node.val))
                    adjency_list[node.val].append(node.right.val)

                prev_val = data[1]
                adjency_list[node.val].append(prev_val)
                # print(prev_val)
                prev_val = node.val

        time = -1

        
        # print(adjency_list)

        visited = set([0])
        queue = deque()

        queue.append(start)

        while queue:
            time += 1
            # print(queue)

            for i in range(len(queue)):
                check = queue.popleft()

                for value in adjency_list[check]:
                    if value in visited:
                        continue

                    visited.add(value)
                    queue.append(value)

                visited.add(check)
                            

        

        return time

                
                
