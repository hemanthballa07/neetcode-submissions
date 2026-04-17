# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head

        while curr:
            N+=1
            curr = curr.next

        remove = N - n 
        curr = head

        if remove == 0:
            return head.next

        for i in range(N-1):
            if (i+1) == remove:
                curr.next = curr.next.next
                break
            curr = curr.next
        return(head)




        