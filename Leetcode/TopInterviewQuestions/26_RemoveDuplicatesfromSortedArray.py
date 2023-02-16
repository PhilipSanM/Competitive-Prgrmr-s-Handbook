# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 26. Remove Duplicates from Sorted Array -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: February - 16- 2023
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# ====================================================================


# First Approach - Using two pointers
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # [1,1,2]
        #  i   j
        k = 1
        index = 0
        for index_comparation in range(1,len(nums) ):
            if nums[index] != nums[index_comparation]:
                index += 1
                nums[index] = nums[index_comparation]
                k += 1
            
        return k


# Second approach  - Using a set
# Time Complexity : O(nlogn)
# Space Complexity: O(n)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        numbers_without_duplicates = set()
        for num in nums:
            numbers_without_duplicates.add(num)
        
        i=0
        numbers_without_duplicates_sorted = list(numbers_without_duplicates)
        numbers_without_duplicates_sorted.sort()
        for num in numbers_without_duplicates_sorted:
            nums[i] = num
            i += 1
        return len(numbers_without_duplicates)


# POST: https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/3194251/python-3-two-easy-solutions-using-set-iterating-through-the-array/
