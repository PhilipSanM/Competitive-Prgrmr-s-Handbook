# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=1704. Determine if String Halves Are Alike -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: January - 11- 2024
# URL: https://leetcode.com/problems/determine-if-string-halves-are-alike/
# ====================================================================

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # "book"    len = 4  also for the middle 4/2 = 2
        # i = 0 , j = 4/2 = 2

        def isVowel(letter):
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                return True

            return False

        first = 0
        s = s.lower()
        second = 0
        i = 0
        j = len(s)//2
        for _ in range(len(s) // 2):
            if isVowel(s[i]):
                first += 1
            
            if isVowel(s[j]):
                second += 1
            
            
            i += 1
            j += 1
        

        return first == second