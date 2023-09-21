# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=83. Remove Duplicates from Sorted List -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: September - 20- 2023
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# ====================================================================

# Using Two pointers
# Time Complexity : O(n)
# Space Complexity: O(1)
# Runtime: 19 ms - Beats: 80.57% <> Memory: 13.22 MB - Beats: 80.44%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first  = head
        second = head.next
        while first:
            while second and first.val == second.val:
                second = second.next
            first.next = second
            first = first.next
            if second:
                second = second.next
            
        

        return head

