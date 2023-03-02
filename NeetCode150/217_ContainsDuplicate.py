# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 217. Contains Duplicate -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: March - 03 - 2023
# URL: https://leetcode.com/problems/contains-duplicate/
# ====================================================================


# First Approach - Using a hash-map
# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
   
        aux = {}
        for num in nums:
            if num in aux:
                return True
            else:
                aux[num] = 1
        return False



# POST: https://leetcode.com/problems/contains-duplicate/solutions/3247939/python3-easy-hashmap/