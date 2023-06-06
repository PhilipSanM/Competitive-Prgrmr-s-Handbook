# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 19. Remove Nth Node From End of List -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: June - 06 - 2023
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# ====================================================================


# First Approach - Iterationg all the list
# Time Complexity : O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Iterate in the list one time to know the size
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        stop = size - n
        prev = head
        if stop == 0:
            # Beginining of the list
            head = head.next

        elif stop == size - 1:
            #Last node
            for _ in range(stop - 1):
                prev = prev.next
            
            prev.next = None
        else:
            #Another node
            for _ in range(stop - 1):
                prev = prev.next
            prev.next = prev.next.next
            
        return head

