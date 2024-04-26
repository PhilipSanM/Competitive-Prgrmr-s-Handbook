# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 305. Number of Islands II -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: April - 26 - 2024
# URL: https://leetcode.com/problems/number-of-islands-ii/
# ====================================================================

class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, node1):
        p = self.parent[node1]

        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False


        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1

        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1

        return True

    def is_connected(self,node1, node2):
        return self.find(node1) == self.find(node2)




class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = UnionFind(m * n)

        neighboors = [[0,1], [0, -1], [1, 0], [-1, 0]]
        
        grid = []
        for i in range(m):
            row = []
            for i in range(n):
                row.append(0)

            grid.append(row)

        answer  = []
        ilands = 0
        mapp = []
        row = []

        for i in range(1, m*n + 1):
            row.append(i)
            if len(row) >= n:
                mapp.append(row)
                row = []

        for row_land, column_land in positions:
            if grid[row_land][column_land] == 1:
                answer.append(ilands)
                continue
            grid[row_land][column_land] = 1
            
            resultant = 0

            for x_neig, y_neig in neighboors:
                if min(row_land + x_neig, column_land + y_neig) < 0 or (row_land + x_neig) >= m or (column_land + y_neig) >= n:
                    continue

                
                if grid[row_land + x_neig][column_land + y_neig] == 1:
                    
                    if not dsu.is_connected(mapp[row_land][column_land], mapp[row_land + x_neig][column_land + y_neig]):
                        resultant += 1
                        dsu.union(mapp[row_land][column_land], mapp[row_land + x_neig][column_land + y_neig])
            
            ilands += 1 - resultant
            answer.append(ilands)

                
                    
            

        return answer
            

