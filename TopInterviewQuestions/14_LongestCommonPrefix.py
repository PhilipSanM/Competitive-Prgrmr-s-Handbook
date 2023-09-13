# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 14. Longest Common Prefix-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: september - 09- 2023
# URL: https://leetcode.com/problems/longest-common-prefix/
# ====================================================================

# First Approach - Hashmap
# Time Complexity : O(nlogn)
# Space Complexity: O(min(m,n)


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                longest += first[i]
            else:
                break
        return longest