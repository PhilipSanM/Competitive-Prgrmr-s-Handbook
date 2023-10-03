# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1512. Number of Good Pairs -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: October - 02- 2023
# URL: https://leetcode.com/problems/number-of-good-pairs/
# ====================================================================

# First Approach - Using a set
# Time Complexity : O(n)
# Space Complexity: O(n)
# Runtime: 14 ms - Beats: 79.38% <> Memory: 12.95 MB - Beats: 98.41%


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        good_pairs = 0
        for number in nums:
            if number not in dic:
                dic[number] = []
            else:
                dic[number].append(1)
                good_pairs += len(dic[number])
        
        return good_pairs