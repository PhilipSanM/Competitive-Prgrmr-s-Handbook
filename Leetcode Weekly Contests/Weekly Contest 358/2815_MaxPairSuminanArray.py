# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 2816. Double a Number Represented as a Linked List -=
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: August - 12 - 2023
# URL: https://leetcode.com/problems/max-pair-sum-in-an-array/
# ====================================================================


# First Approach - Hash-map
# Time Complexity : O(n)
# Space Complexity: O(n)

# Runtime: 93ms Beats 100.00%of users with Python ; Memory: 16.34mb Beats 66.67%of users with Python


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic  ={}
        res = -1
        for number in nums:
            string_num = str(number)
            max_digit  = max(string_num)
            if max_digit in dic:
  
                res = max(res, number + dic[max_digit])
                better = max(number, dic[max_digit])
                dic[max_digit] = better

            else:
                dic[max_digit] = number
            
        
        return res
        