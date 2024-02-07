# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-451. Sort Characters By Frequency -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 07- 2024
# URL: https://leetcode.com/problems/sort-characters-by-frequency
# ====================================================================

class Solution:
    def frequencySort(self, s: str) -> str:
        frequencys = {}

        for letter in s:
            frequencys[letter] = frequencys.get(letter, 0) + 1

        sorting = []

        for letter,frequency in frequencys.items():
            sorting.append((frequency, letter))

        sorting.sort(reverse = True)

        answer = ""

        for letter,frequency in sorting:
            answer += letter * frequency


        return answer