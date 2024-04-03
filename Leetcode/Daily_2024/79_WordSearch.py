# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 79. Word Search -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: April - 02- 2024
# URL: https://leetcode.com/problems/word-search/
# ====================================================================

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, column, visited, index):
            if index >= len(word):
                return True

            if (row, column) in visited or min(row, column) < 0 or row >= len(board) or column >= len(board[0]):
                return False

            if board[row][column] != word[index]:
                return False

            visited.add((row,column))

            if dfs(row + 1, column, visited, index + 1) or dfs(row - 1, column, visited, index + 1) or dfs(row, column + 1, visited, index + 1) or dfs(row, column - 1, visited, index + 1):
                return True



            visited.remove((row, column))

            return False


        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0]:
                    if dfs(row, column, set(), 0):
                        return True


        return False        


# "ABCESEEEFS"
# [["A","B","C","E"],
# ["S","F","E","S"],
# ["A","D","E","E"]]