# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-1992. Find All Groups of Farmland -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 20- 2024
# URL: https://leetcode.com/problems/find-all-groups-of-farmland/
# ====================================================================

class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        lands = []
        visited = set()

        def dfs(row, column, visited):
            if min(row, column) < 0 or row >= len(land) or column >=len(land[0]) or (row, column) in visited or land[row][column] == 0:
                return [0,0]

            visited.add((row, column))
            
            return [max(row, dfs(row + 1, column, visited)[0]), max(column, dfs(row, column + 1, visited)[1])]

            


        for row in range(len(land)):
            for column in range(len(land[0])):
                if land[row][column] == 1 and (row, column) not in visited:
                    top_right = dfs(row, column, visited)
                    lands.append([row, column, top_right[0], top_right[1]])
                    
                    

        return lands