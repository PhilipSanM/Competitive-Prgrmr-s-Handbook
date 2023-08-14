# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 2816. Double a Number Represented as a Linked List -=
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: August - 12 - 2023
# URL: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
# ====================================================================


# First Approach - Rercursion
# Time Complexity : O(n)
# Space Complexity: O(1)

# Runtime: 471ms Beats 100.00%of users with Python ; Memory: 29.94mb Beats 100.00%of users with Python


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def helper(head):
            if not head.next:
                value = head.val * 2
                carry = 1 if value >= 10 else 0
                head.val = value % 10
                # print('lalalala')
                # print(carry)
                return carry
            
            carry = helper(head.next)
            value = head.val * 2 + carry
            carry = 1 if value >= 10 else 0
            head.val = value % 10
            return carry
        
        carry = helper(head)
        # print(carry)
        if carry == 1:
            xd = ListNode(carry)
            xd.next = head
            return xd
        return head 
        