import sys
from Sol import Solution

# Open output file
sys.stdout = open('outputf.in', 'w')

# Code goes here

solution = Solution()
print(solution.uniquePaths(3,2))





# close output file
sys.stdout.close()