# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head = [1,2,3,4,5]
        #                 i
        # size = 5
        # 
        
        # point_head = head
        # prev = None

        # while point_head:
        #     aux = point_head.next
        #     point_head.next = prev
        #     prev = point_head
        #     point_head = aux

        # return prev

        # ===============================
        # recursive case
        # ===============================
        # head = [1,2,3,4,5]
        #         _________      i
        if not head:
            return None
        res = head
        if head.next:
            res = self.reverseList(head.next)
            head.next.next = head
            
        head.next = None
        return res








