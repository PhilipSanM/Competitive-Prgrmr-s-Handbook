# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 232. Implement Queue using Stacks -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: January - 29- 2024
# URL: https://leetcode.com/problems/implement-queue-using-stacks/
# ====================================================================



# queue:
# <- [1, 2, 3, 4] <-

# stack
# [1, 2, 3, 4] <->

# queue
# [4, 3, 2, 1]


class MyQueue(object):

    def __init__(self):
        self.queue = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)        

    def pop(self):
        """
        :rtype: int
        """
        
        if not self.queue:
            while self.stack:
                self.queue.append(self.stack.pop())

        return self.queue.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.queue:
            while self.stack:
                self.queue.append(self.stack.pop())
        
        return self.queue[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return max(len(self.queue), len(self.stack)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()