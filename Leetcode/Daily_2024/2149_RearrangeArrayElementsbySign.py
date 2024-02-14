# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 2149. Rearrange Array Elements by Sign -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 13- 2024
# URL: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
# ====================================================================

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_index = 0
        negative_index = 1

        result = nums[:]
        for num in nums:
            if num > 0:
                position = positive_index
                positive_index += 2

            else:
                position = negative_index
                negative_index += 2

            result[position] = num

        return result


