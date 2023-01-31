
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=- T W O - S U M =-=-=-=-=-=-=-==-=-=-=-=-=-=
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: January - 31 - 2023
# URL: https://leetcode.com/problems/two-sum/
# ====================================================================
#
# 
#  My Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        index_num1 = -1
        for num1 in nums:
            index_num1 += 1
            left_over = target - num1
            if left_over in nums:
                index_left_over = nums.index(left_over)
                if index_num1 is not index_left_over:
                    answer.append(index_num1)
                    answer.append(index_left_over)
                    return answer
    
# Time complexity: O(n)
# Space complexity: O(n)

# -------------  O P T I M I Z E D by arajAnkit -----------------------
# Using a hashmap

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            left_over = target - nums[i] 
            if left_over in map:
                return [map[left_over],i]
            else:
                map[nums[i]] = i

# Time complexity: O(N)
# Space Complexity: O(N)