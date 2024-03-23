# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head.next
        stack = deque()

        while curr:
            stack.append(curr)
            curr = curr.next

        

        curr = head

        for i in range(len(stack)):
            if i % 2 == 0:
                curr.next = stack.pop()
            else:
                curr.next = stack.popleft()

            curr = curr.next

        curr.next = None

