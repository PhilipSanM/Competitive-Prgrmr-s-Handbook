# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 49. Group Anagrams -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 06- 2024
# URL: https://leetcode.com/problems/group-anagrams/
# ====================================================================

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:
            letters = [0]*26

            for letter in word:
                letters[ord(letter) - ord('a')] += 1

            letters = tuple(letters)

            if letters not in anagrams:
                anagrams[letters] = [word]
            else:
                anagrams[letters].append(word)


        
        return anagrams.values()
        