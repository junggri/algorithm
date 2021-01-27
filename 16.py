def reverseList(self, head):
    rev = None

    if not head:
        return rev

    slow = head
    while slow:
        rev, rev.next, slow = slow, rev, slow.next
    print(rev)
    return rev
