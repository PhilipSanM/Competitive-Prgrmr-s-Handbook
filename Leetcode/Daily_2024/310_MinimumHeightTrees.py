# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-279. Perfect Squares-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 22- 2024
# URL: https://leetcode.com/problems/minimum-height-trees/
# ====================================================================

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adj = {i: set() for i in range(n)}

        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])

        # leafs
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)


        total_nodes = n
        
        while total_nodes > 2:
            total_nodes -= len(leaves)

            new_leaves = []
            for leaf in leaves:
                # here there is only one node that is neighbor
                father = adj[leaf].pop()
                adj[father].remove(leaf)

                # adding new leaves
                if len(adj[father]) == 1:
                    new_leaves.append(father)

            leaves = new_leaves

        return leaves
            

        