# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-1544. Make The String Great -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: April - 04 - 2024
# URL: https://leetcode.com/problems/make-the-string-great/description/
# ====================================================================

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for letter in s:
            if stack and stack[-1].lower() == letter.lower() and (stack[-1].islower() and letter.isupper()  or stack[-1].isupper() and letter.islower()  ):

                stack.pop()
            else:
                stack.append(letter)

            


        return ''.join(stack)