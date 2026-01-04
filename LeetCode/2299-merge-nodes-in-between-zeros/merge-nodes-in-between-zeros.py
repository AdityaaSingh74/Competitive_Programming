# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr.next != None:
            summ = 0
            prevptr = ptr
            ptr = ptr.next
            while (ptr.val != 0):
                summ += ptr.val
                ptr = ptr.next
            prevptr.val = summ
            prevptr.next = ptr
        prevptr.next = None
        return head
