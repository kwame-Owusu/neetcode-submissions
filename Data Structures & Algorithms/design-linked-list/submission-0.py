class ListNode():
    def __init__(self, val = -1, prev = None, next = None ):
        self.prev = prev
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode() # dummy head
        self.tail = ListNode() # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1

        curr = self.head.next
        i = 0

        while i < index:
            curr = curr.next
            i += 1

        return curr.val


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None
        
        curr = self.head
        i = 0

        # traverse until we find the node
        while i < index:
            curr = curr.next
            i += 1
        
        new_node = ListNode(val)
        new_node.next = curr.next
        new_node.prev = curr
        curr.next.prev = new_node
        curr.next = new_node
        
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        
        curr = self.head.next
        i = 0

        # traverse until we find the node
        while i < index:
            curr = curr.next
            i += 1
        
        prev_node = curr.prev # curr is now node we want to drop
        next_node = curr.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)