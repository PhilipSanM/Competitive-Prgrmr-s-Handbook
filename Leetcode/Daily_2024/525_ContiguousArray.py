# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=- 525. Contiguous Array =-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 15 - 2024
# URL: https://leetcode.com/problems/contiguous-array/
# ====================================================================


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # It's fuccking using a hashmap
        # [0  ,  1]
        #        |
        # count = 0
        # coount - index
        #  cache{  
        #    0 : -1
        #    -1 : 0
        # 
        # }

        count = 0
        cache = {
            0: -1
        }
        longest = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in cache:
                longest = max(longest, i - cache[count])

            else:
                cache[count] = i

        return longest