input = [1, 2, 3, 4]


class LinkNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None


def makeList(input):
    list = LinkList()
    for i in range(len(input)):
        node = LinkList()
        if i == 0:
            node.val = i
            node.next = 'node%s+1' % i
            list.head = node
        elif i == len(input) - 1:
            node.val = i
            node.next = None
        else:
            node.val = i
            node.next = 'node%s+1' % i
        print(node)
        ㅇ


a = makeList(input)
