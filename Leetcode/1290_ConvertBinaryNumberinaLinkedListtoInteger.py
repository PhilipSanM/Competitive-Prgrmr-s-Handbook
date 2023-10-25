# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1290. Convert Binary Number in a Linked List to Integer -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: October - 24- 2023
# URL: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# ====================================================================

# First Approach - Just iterating over the list
# Time Complexity : O(2n)
# Space Complexity: O(1)
# Runtime: 4 ms - Beats: 99.40% <> Memory: 13.3 MB - Beats: 39.88%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        size = 0

        pointer = head

        while pointer:
            size += 1
            pointer = pointer.next

        pointer = head
        size -= 1

        res = 0
        while pointer:
            if pointer.val == 1:

                res += 2 ** size
            size -= 1
            pointer = pointer.next

        return res
