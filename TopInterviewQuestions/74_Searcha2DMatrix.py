# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-= 74. Search a 2D Matrix -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: July - 26- 2023
# URL: https://leetcode.com/problems/search-a-2d-matrix/
# ====================================================================

# Using full binary seach and binary search in range
# Time Complexity : O(logmn)
# Space Complexity: O(1)
# Runtime: 27 ms - Beats: 79.42% <> Memory: 13.7 MB - Beats: 44.21%

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Observations:
        #  1.- We can have the last value and the first
        #  2.- We dont care if the first value is already the target


        #    [1    3     5     7]  l
        #    [10   11   16    20]  mid
        #    [23   30   34    60]   r

        # edge cases:   m   
        #   input =   [[ 1 ] ] n
        #   target not in range
        if not matrix or not matrix[0]:
            return False

        def isInRange(low, high, target):
            if low <= target and target <= high:
                return 0
            elif high < target:
                return 1
            elif low > target:
                return -1
            

        #  [[ 1 ] ]
        # l = 0 , r = 1  t = 2, mid = 0

        def findRow(matrix, target):
            # To do
            l, r = 0 , len(matrix) - 1
            while l <= r:
                mid = (l + r) //2
                if isInRange(matrix[mid][0], matrix[mid][-1], target) > 0:
                    l = mid + 1
                elif isInRange(matrix[mid][0], matrix[mid][-1], target) < 0:
                    r = mid  - 1
                else:
                    return mid

            return 0
            



        row = findRow(matrix, target)


        def binarySearch(numbers, target):
            l,r = 0,len(numbers) -1

            while l <= r:
                mid = ( l + r)//2
                if numbers[mid] < target:
                    l = mid + 1
                elif numbers[mid] > target:
                    r = mid - 1
                else:
                    return True

            return False


        return binarySearch(matrix[row], target)

