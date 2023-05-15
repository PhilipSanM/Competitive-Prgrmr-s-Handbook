# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1472. Design Browser History -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: May - 15 - 2023
# URL: https://leetcode.com/problems/design-browser-history/description/
# ====================================================================


# Time Complexity : O(n)
# Space Complexity: O(n)


# # Double Linked list
class page_node(object):
    def __init__(self, page):
        self.url = page
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        head = page_node(homepage)
        self.current = head
        
# Time Complexity : O(1)
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        next_page = page_node(url)
        self.current.next = next_page
        next_page.prev = self.current
        self.current = next_page

# Time Complexity : O(n)    
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.current.prev and steps > 0:
            steps = steps - 1
            self.current = self.current.prev
        

                
        return self.current.url
        
# Time Complexity : O(n)
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.current.next and steps > 0:
            steps = steps - 1
            self.current = self.current.next

        return self.current.url
        
# Using a list = array

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Using a list = array
# Time Complexity : O(1)
# Space Complexity: O(n)

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.index = 0
        self.len = 1
        self.history = [homepage]
        
# Time Complexity : O(1)
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """

        if len(self.history) == self.index + 1:
            self.history.append(url)
        else:
            self.history[self.index + 1] = url
        
        self.index = self.index + 1
        self.len = self.index + 1
    
# Time Complexity : O(1)
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.index = max(self.index - steps, 0)
        return self.history[self.index]
        
# Time Complexity : O(1)
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.index = min(self.index + steps, self.len - 1)
        return self.history[self.index]

        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)