# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-1481. Least Number of Unique Integers after K Removals -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 15 - 2024
# URL: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# ====================================================================

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequencies = {}

        for num in arr:
            frequencies[num] = frequencies.get(num, 0) + 1

        # sorted by frecuency
        unique_numbers = sorted(frequencies, key = lambda x: frequencies[x])
        
        i = 0

        while i < len(unique_numbers) and k - frequencies[unique_numbers[i]] >= 0:
            k -= frequencies[unique_numbers[i]]
            i += 1




        return len(unique_numbers) - i