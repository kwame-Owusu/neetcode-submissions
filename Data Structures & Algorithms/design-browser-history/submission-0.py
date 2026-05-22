class ListNode():
    def __init__(self, val = ""):
        self.val = val # url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.curr
        self.curr.next = node
        self.curr = node

    def back(self, steps: int) -> str:
        while self.curr.prev is not None and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next is not None and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)