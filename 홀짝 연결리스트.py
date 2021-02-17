# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        even = head.next
        even_head = head.next
        while odd and odd.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next;
            even = even.next
        odd.next = even_head
        return head
