# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        res = []
        curr = head

        while curr:
            res.append(curr.val)
            curr = curr.next 
        
        res = res[::-1]
        dummy = ListNode(res[0])
        curr = dummy

        for val in res[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy