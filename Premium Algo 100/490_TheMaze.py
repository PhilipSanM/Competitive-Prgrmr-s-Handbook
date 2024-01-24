# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 490. The Maze -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 23 - 2023
# URL: https://leetcode.com/problems/the-maze/
# ====================================================================

'''                       

Restrictions:
    - the borders
    - the goal
                        [start]
                 /       |     |      \ 
                [up]  [down] [right] [left]
              / | | \
               [goal, stoped?]

    - you stop because you are going to the left, and the wall is at the left
            
         column     1
# [ row [0, 0, 1, *, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0 ,0, 0, *] ]


'''
import copy
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        def doBallStoped(row, column, direction):
            if direction == 'left' and column<= 0 or direction == 'left' and maze[row][column - 1] == 1:
                return True
            
            if direction == 'right' and column>= len(maze[0]) - 1 or direction == 'right' and maze[row][column + 1] == 1:
                
                return True

            if direction == 'up' and row <= 0 or direction == 'up' and maze[row - 1][column] == 1:
                return True

            if direction == 'down' and row>= len(maze) - 1 or direction == 'down' and maze[row + 1][column] == 1:
                return True

            return False

            # row, col
        movements = {
            'left' : [0, -1],
            'right': [0, 1],
            'up': [-1, 0],
            'down': [1, 0]
        }



        def backtrack(row, column, direction, cache):
            # print(row, column, direction)

            if (row, column, direction) in cache:
                return cache[(row, column, direction)]

            # Out of maze
            if min(row, column) < 0 or row >= len(maze) or column >= len(maze[0]):
                return False       
            elif row == destination[0] and column == destination[1] and doBallStoped(row, column, direction):
                # print('ALAVERGA')
                return True
            elif not doBallStoped(row, column, direction):
                cache[(row, column, direction)] = False
                return backtrack(row + movements[direction][0], column + movements[direction][1], direction, cache)
            else:
                # print('paraaa')
                directions = ['left', 'right', 'up', 'down']
                for curr in directions:
                    if doBallStoped(row, column, curr):
                        cache[(row, column, direction)] = False
                        continue
                    if backtrack(row + movements[curr][0], column + movements[curr][1], curr, cache):
                        return True
                    
                 


            return False


        return backtrack(start[0], start[1], 'left', {}) or backtrack(start[0], start[1], 'right', {}) or backtrack(start[0], start[1], 'up', {}) or backtrack(start[0], start[1], 'down', {})
