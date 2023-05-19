# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 36. Valid Sudoku -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: May - 18 - 2023
# URL: https://leetcode.com/problems/valid-sudoku/
# ====================================================================


# First Approach - 
# Time Complexity : O(n^2) = O(9^2) in most efficient algorithms
# Space Complexity: O(n)
# First brute force solution
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            rows = {}
            for num in row:
                if num in rows and num != ".":
                    
                    return False
                else:
                    rows[num] = 0

        for i in range(9):
            columns = {}
            for j in range(9):
                if board[j][i] in columns and board[j][i] != ".":
                    return False
                else:
                    columns[board[j][i]] = 0

        squareA = {}
        squareB = {}
        squareC = {}
        for i in range(0, 3): 
            for j in range(0, 3): 
                if board[j][i] in squareA and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareA[board[j][i]] = 0

            for j in range(3, 6): 
                if board[j][i] in squareB and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareB[board[j][i]] = 0

            for j in range(6, 9): 
                if board[j][i] in squareC and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareC[board[j][i]] = 0

        
        squareA = {}
        squareB = {}
        squareC = {}
        for i in range(3, 6): 
            for j in range(0, 3): 
                if board[j][i] in squareA and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareA[board[j][i]] = 0

            for j in range(3, 6): 
                if board[j][i] in squareB and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareB[board[j][i]] = 0

            for j in range(6, 9): 
                if board[j][i] in squareC and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareC[board[j][i]] = 0

        
        squareA = {}
        squareB = {}
        squareC = {}
        for i in range(6, 9): 
            for j in range(0, 3): 
                if board[j][i] in squareA and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareA[board[j][i]] = 0

            for j in range(3, 6): 
                if board[j][i] in squareB and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareB[board[j][i]] = 0

            for j in range(6, 9): 
                if board[j][i] in squareC and board[j][i] != ".":
                    print("aqi")
                    return False
                else:
                    squareC[board[j][i]] = 0
        return True



# More efficent:


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """


        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = {(j, i): set() for i in range(3) for j in range(3)}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3 , c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r //3 , c//3)].add(board[r][c])
        return True