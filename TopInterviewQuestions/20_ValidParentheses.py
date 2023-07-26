# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-      20. Valid Parentheses    -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: February - 16- 2023
# URL: https://leetcode.com/problems/valid-parentheses/description/
# ====================================================================


# First Approach Using a stack
# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # First approach using a stack
        stack = []
        for parenthesis in s:
            if parenthesis in ('(', '[', '{'):
                stack.append(parenthesis)
            else:
                if stack == []:
                    return False
                else:
                    if parenthesis == ')':
                        if stack.pop() == '(':
                            continue
                        else:
                            return False
                    elif parenthesis == '}':
                        if stack.pop() == '{':
                            continue
                        else:
                            return False
                    elif parenthesis == ']':
                        if stack.pop() == '[':
                            continue
                        else:
                            return False

        return stack == []

# POST: https://leetcode.com/problems/valid-parentheses/solutions/3195174/python-3-beats-99-72-using-a-stack/