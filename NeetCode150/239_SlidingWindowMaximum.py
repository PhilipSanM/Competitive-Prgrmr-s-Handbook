# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 238. Product of Array Except Self-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: March - 03 - 2023
# URL: https://leetcode.com/problems/product-of-array-except-self/description/
# ====================================================================


# First Approach - Iterating two time in an array
# Time Complexity : O(n)
# Space Complexity: O(n)
#checking all the values multiplicated before and after



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums = [1,2,3,4]
        #         [1, 1 , 2 , 6]
        ans = []
        prefix = 1
        ans.append(prefix)
        for i in range(0, len(nums) - 1):
            prefix *= nums[i]
            ans.append(prefix)

#       print(ans)
        sufix = 1
        # nums = [1,2,3,4]
        #            2*12       4*3
        #         [1* 24, 1* 12 , 2 * 4, 6 * 1]
        for i in range(len(nums) -1, -1, -1):
            ans[i] = ans[i] * sufix
            sufix *= nums[i]

#        print(ans)
        return ans

        # All the values from one side to the other

            
