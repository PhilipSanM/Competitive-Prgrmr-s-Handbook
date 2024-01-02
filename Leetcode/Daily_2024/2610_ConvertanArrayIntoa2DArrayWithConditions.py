# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 455. Assign Cookies -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 2- 2024
# URL: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
# ====================================================================

class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        frequency = {}
        matrix = []
        
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 0
            # frequency[num] = frequency.get(num, 0) + 1

            # index = frequency[num] - 1
            index = frequency[num]

            if index >= len(matrix):
                matrix.append([])

            matrix[index].append(num)


        return matrix