# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1056. Confusing Numbers -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: January - 23 - 2023
# URL: hhttps://leetcode.com/problems/confusing-number/
# ====================================================================


class Solution:
    def confusingNumber(self, n: int) -> bool:
        valid_numbers = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        number_2_string = str(n)

        confusing = ""
        for char in number_2_string:
            if char not in valid_numbers:
                # print(char)
                return False

            confusing = valid_numbers[char] + confusing


        # print(confusing, number_2_string)
        return confusing != number_2_string

                    