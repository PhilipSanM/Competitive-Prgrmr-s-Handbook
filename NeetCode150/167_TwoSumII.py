# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 167. Two Sum II - Input Array Is Sorted -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: May - 23 - 2023
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# ====================================================================


# First Approach - Using a binary search
# Time Complexity : O(nlogn)
# Space Complexity: O(1)


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            left_over = target - numbers[i]
            index = self.binarySearch(numbers,left_over)
            if index != i  and index != -1:
                if index > i:
                    return [i + 1, index + 1]
                else:
                    return [index + 1, i + 1]
            





    # [2,7,8,9,11,15]
    #      m l      r
    def binarySearch(self, numbers,target):
        l,r = 0, len(numbers) - 1
        while l <= r:
            mid = (l+r)//2
            if target > numbers[mid]:
                l = mid + 1
            elif target < numbers[mid]:
                r = mid - 1
            else:
                return mid
        
        return -1


# Second Approach - Using two pointers
# Time Complexity : O(n)
# Space Complexity: O(1)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0, len(numbers) - 1
        while l <= r:
            two_sum = numbers[l] + numbers[r]
            if target > two_sum:
                l += 1
            elif target < two_sum:
                r -= 1
            else:
                return [l + 1, r+ 1]





    # [2,7,8,9,11,15]
    #      m l      r
    def binarySearch(self, numbers,target):
        l,r = 0, len(numbers) - 1
        while l <= r:
            mid = (l+r)//2
            if target > numbers[mid]:
                l = mid + 1
            elif target < numbers[mid]:
                r = mid - 1
            else:
                return mid
        
        return -1