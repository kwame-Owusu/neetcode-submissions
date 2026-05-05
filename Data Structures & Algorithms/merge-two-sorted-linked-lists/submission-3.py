# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        array1 = []
        array2 = []

        merged_lists = []

        curr = list1

        while curr:
            array1.append(curr.val)
            curr = curr.next
        
        curr = list2
        while curr:
            array2.append(curr.val)
            curr = curr.next
        
        merged_lists = array1 + array2
        merged_lists.sort()

        dummy = ListNode(merged_lists[0])
        curr = dummy

        for val in merged_lists[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy
        #time complexity = O(n)
        #space complexity = O(n)