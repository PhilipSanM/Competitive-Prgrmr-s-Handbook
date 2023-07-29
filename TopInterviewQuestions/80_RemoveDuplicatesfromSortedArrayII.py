# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-= 80. Remove Duplicates from Sorted Array II -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: July - 29- 2023
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
# ====================================================================

# Using Two pointers
# Time Complexity : O(n)
# Space Complexity: O(1)
# Runtime: 33 ms - Beats: 89.95% <> Memory: 13.43 MB - Beats: 19.47%


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,   0,    1,   1,    2,    3,   3,   3,  3 ]
        #                                  L             R 
        # count = 2         
        #  Swaps
        # return =  L
        L,R = 0, 0 

        while R < len(nums):
            count = 1

            while R + 1 < len(nums) and nums[R] == nums[ R+1 ]:
                count += 1
                R += 1

            for i in range(min(2, count)):
                nums[L] = nums[R]
                L += 1
            R+= 1

        return L