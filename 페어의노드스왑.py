# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        list = None
        while head and head.next:
            node1 = ListNode(head.next.val)
            node2 = ListNode(head.val)
            node1.next = node2
            if not list:
                list = node1
            else:
                list.next.next = node1
            head = head.next.next
        return list
