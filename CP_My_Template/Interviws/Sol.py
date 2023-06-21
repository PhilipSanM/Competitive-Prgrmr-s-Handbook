class Solution(object):
    def __init__(self):
        pass

    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Using DP        
        """
         _ _
        |_|_|
        |_|_|
        |_|_|
        
        """
        prevRow = [1] * n

        for i in range(m - 2, -1, -1):
            curRow = [0] * n
            # Puting one at the begining 
            curRow[n -1] = 1
            for j in range( n - 2, -1, -1):
                curRow[j] = prevRow[j] + curRow[j + 1]
            
            prevRow = curRow
        
        return prevRow[0]