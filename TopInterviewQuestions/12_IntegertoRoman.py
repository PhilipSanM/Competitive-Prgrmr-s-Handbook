
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-      12. Integer to Roman     -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: Juli - 03- 2023
# URL: https://leetcode.com/problems/integer-to-roman/description/
# ====================================================================


# First Approach
# Time Complexity : O(1)
# Space Complexity: O(1)

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII","IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX","XC"] 
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["","M", "MM", "MMM"]

        return thousands[(num%10000)//1000] + hundreds[(num%1000)//100] + tens[(num%100)//10] + ones[num%10]