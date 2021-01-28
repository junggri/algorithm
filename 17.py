# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(list):
            arr = []
            if not list:
                return 0
            while list:
                arr.append(list.val)
                list = list.next
            return "".join(map(str, arr[::-1]))

        num1 = reverseList(l1)
        num2 = reverseList(l2)

        sum_arr = str((int(num1) + int(num2)))
        rev = None
        for i in range(0, len(sum_arr)):
            print(sum_arr[i])
            node = ListNode(sum_arr[i])
            node.next = rev
            rev = node
