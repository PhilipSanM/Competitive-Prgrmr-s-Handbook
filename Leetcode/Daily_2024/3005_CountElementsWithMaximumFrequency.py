# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=3005. Count Elements With Maximum Frequency-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: March - 07- 2024
# URL: https://leetcode.com/problems/count-elements-with-maximum-frequency/
# ====================================================================\

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequencies = {}
        max_frequency = 0
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            max_frequency = max(max_frequency, frequencies[num])

        

        elements = 0

        for key, freq in frequencies.items():
            if freq == max_frequency:
                elements += 1

        return elements * max_frequency
        
        