# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=1971. Find if Path Exists in Graph -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: April - 20- 2024
# URL: https://leetcode.com/problems/find-if-path-exists-in-graph/
# ====================================================================


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        adj = {}

        for i in range(n):
            adj[i] = []

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])


        queue = deque([source])
        visited = set([source])

        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                next_nodes = adj[curr_node]

                for node in next_nodes:
                    if node == destination:
                        return True
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)

        
        return False