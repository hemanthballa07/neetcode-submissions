# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        first = head
        second = prev
        dummy = ListNode(0)
        tail = dummy
        while first and second:
            tail.next = first
            first = first.next
            tail.next.next = second
            tail = second
            second = second.next
        if first:
            tail.next = first
        else:
            tail.next = second
        head = dummy.next

        

        