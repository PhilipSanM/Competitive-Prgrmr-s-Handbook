# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 242. Valid Anagram -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: March - 03 - 2023
# URL: https://leetcode.com/problems/valid-anagram/
# ====================================================================


# First Approach - Using a hash-map
# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # First approach using a hashmap, or in py a dictionary with an int value


        if len(t) != len(s):
            return False
        
        key = {}
        for letter in s:
            if letter in key:
                key[letter] += 1
            else:
                key[letter] = 1
    
        for letter in t:
            if letter not in key or key[letter] < 1:
                return False
            else:
                key[letter] -= 1

        return True

# POST: https://leetcode.com/problems/valid-anagram/solutions/3247950/python-3-easy-using-hashmap/