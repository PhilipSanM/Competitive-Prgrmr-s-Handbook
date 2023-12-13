# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 43. Multiply Strings=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: December - 12- 2023
# URL: https://leetcode.com/problems/multiply-strings/description/
# ====================================================================

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        numbers = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }

        reversed_numbers = {}

        for key, value in numbers.items():
            reversed_numbers[value]  = key
        
        def cast_string2integer(num):
            integer = 0
            auxiliar = 10**len(num)
            for digit in num:
                auxiliar /= 10
                integer += numbers[digit] * auxiliar
                
            return integer

        integer_num1 = cast_string2integer(num1)
        integer_num2 = cast_string2integer(num2)

        multiplication = integer_num1*integer_num2
        conversion = ""

        if multiplication == 0:
            return reversed_numbers[multiplication]

        while multiplication > 0:
            resultant = multiplication % 10

            multiplication = multiplication//10

            conversion = reversed_numbers[resultant] + conversion



        return conversion
