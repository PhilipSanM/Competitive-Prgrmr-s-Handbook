# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=- 22540. Minimum Common Value -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: March - 08 - 2024
# URL: https://leetcode.com/problems/minimum-common-value/
# ====================================================================

class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        first, second = 0, 0

        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                return nums1[first]

            elif nums1[first] < nums2[second]:
                first += 1

            else:
                second += 1


        return -1
        