# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 187. Repeated DNA Sequences -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: Nov - 27 - 2023
# URL: https://leetcode.com/problems/repeated-dna-sequences/description/
# ====================================================================



# Sliding window
# Time Complexity : O(n)
# Space Complexity: O(n)



class Solution(object):

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequences = set()
        repeated = set()
        i = 0
        while i + 10 <= len(s):
            sequence = s[i : i +10]
            if sequence in sequences:
                repeated.add(sequence)
            sequences.add(sequence)
            i += 1


        return list(repeated)        