# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 645. Set Mismatch-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: January - 22- 2024
# URL: https://leetcode.com/problems/set-mismatch/description/
# ====================================================================

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [1, 2, 3, 4]
        # [1, 2, 2, 4] -> [2, 3]


        # [1, 2, 3, 2] -> [2, 4]

        # [3, 2, 2]
        #  [2, 1]
        # thetre
        repeted = set()
        answer = [-1, -1]
        good_numbers = set([number for number in range(1, len(nums) + 1)])
        for num in nums:
            if num in repeted:
                answer[0] = num        
            repeted.add(num)
            if num in good_numbers:
                good_numbers.remove(num)

        for value in good_numbers:
            answer[1] = value
        
        return answer