# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 27. Remove Element-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: February - 16- 2023
# URL: https://leetcode.com/problems/remove-element/
# ====================================================================


# First Approach - Make a copy and ectend with built in functions
# Time Complexity : O(1)
# Space Complexity: O(n)
# Runtime: 63 ms - Beats: 71.47% <> Memory: 13.6 MB - Beats: 75.68%
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = list(nums)
        ans.extend(nums)
        return ans


# Second approach  - Using a Two pointes again
# Time Complexity : O(1)
# Space Complexity: O(1)
# Runtime: 58 ms ms - Beats: 90.89%% <> Memory: 13.8 MB - Beats: 50.26%

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums

# POST: https://leetcode.com/problems/concatenation-of-array/solutions/3194641/python-3-solution-easy/
