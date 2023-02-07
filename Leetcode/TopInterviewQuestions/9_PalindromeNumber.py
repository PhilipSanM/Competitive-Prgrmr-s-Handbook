# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-      9. Palindrome Number     -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: February - 07- 2023
# URL: https://leetcode.com/problems/palindrome-number/description/
# ====================================================================


# First Approach
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 0
        j = len(x) - 1

        flag = True
        while not i>= j:
            if x[i] != x[j]:
                flag = False
                break
            i += 1
            j -= 1
        return flag

# Second approach using the number in reverse
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False 
        reverse = 0
        cpy = x
        while x > 0 :
            value = x % 10 
            reverse = reverse *10 + value
            x /= 10
        if reverse == cpy:
            return True
        else:
            return False

        # Time Complexity = O(n)
        # Space Complexity = O(n)