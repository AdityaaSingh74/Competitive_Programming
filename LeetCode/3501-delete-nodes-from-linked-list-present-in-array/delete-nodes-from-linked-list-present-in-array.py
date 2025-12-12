# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        setnums = set(nums)
        ptr = head
        prevptr =head
        while ptr != None:
            if ptr.val in setnums:
                if ptr == head:
                    ptr = ptr.next
                    head=ptr
                    continue
                ptr = ptr.next
                prevptr.next = ptr
                continue
            prevptr = ptr
            ptr = ptr.next
        return head