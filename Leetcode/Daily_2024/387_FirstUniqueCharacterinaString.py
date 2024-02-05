# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 387. First Unique Character in a String -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: February - 05- 2024
# URL: https://leetcode.com/problems/first-unique-character-in-a-string/
# ====================================================================

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniques = {}
        index = 0

        repeted = set()

        for letter in s:
            if letter in uniques:
                repeted.add(letter)
                uniques.pop(letter)
            
            if letter not in repeted:
                uniques[letter] = index

            
            index += 1

        # find minimun
        minimun = float('inf')
        first_char = -1

        for letter,position in uniques.items():
            if position < minimun:
                first_char = position
                minimun = position




        return first_char