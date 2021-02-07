# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        rev = head
        prev = None
        i = 1
        while rev:
            if i >= m and i <= n:
                prev, prev.next, rev = rev, prev, rev.next
            else:
                rev = rev.next
            if i == n:
                break
            i += 1

        head.next = prev
        while prev and prev.next:
            prev = prev.next
            if not prev.next:
                prev.next = rev
                break
        return head
