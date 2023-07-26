# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-3. Longest Substring Without Repeating Characters =-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 02 - 2023
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# ====================================================================


#  nettcode sol

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # USING Split in PY

        # "pswfwkew"
        # sub= 'w'
        # best = 'pswf'
        # "asqwertyui"
        sub = ''
        best = ''
        for letter in s:
            if letter in sub:
                if len(best) < len(sub):
                    best = sub
                sub = sub[sub.index(letter) + 1 :] + letter
            else:
                sub += letter
                
        if len(sub) > len(best):
            best = sub
        return len(best)

# Time complexity: O(N)
# Space Complexity: O(N)


# My solution

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_size = 0
        curr_size = 0
        dic_string = {}
        first = 0
        second = 0
        for i in range(0, len(s)):
            if s[second] in dic_string:
                # Loop first point one position next to the repeating char
                # Remove one element in currsize update first poniter until passing repeating o
                while s[second] in dic_string: 
                    dic_string.pop(s[first])
                    curr_size -= 1
                    first += 1
            dic_string[s[second]] = i
            second += 1
            curr_size += 1

            max_size = max(max_size, curr_size)
            


        return max_size