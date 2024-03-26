# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1119. Remove Vowels from a String -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: March - 26 - 2024
# URL: https://leetcode.com/problems/remove-vowels-from-a-string/
# ====================================================================

class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([letter for letter in s if letter not in set('aeiou')])
        