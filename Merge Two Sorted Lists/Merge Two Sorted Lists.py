class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printNode(node):
    result = []
    while node.next:
        result.append(str(node.val))
        node = node.next
    result.append(str(node.val))
    print(result)
    print('->'.join(result))

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        vals1 = self.vals(l1)
        vals2 = self.vals(l2)
        if len(vals1) == 0:
            return l2
        if len(vals2) == 0:
            return l1
        result = []
        vals = vals1 + vals2
        vals.sort()
        for val in vals:
            result.append(ListNode(val))
        for i in range(0, len(result)-1):
            result[i].next = result[i+1]
        return result[0]
    def vals(self, node):
        result = []
        while node.next:
            result.append(node.val)
            node = node.next
        result.append(node.val)
        return result

def main():
    # 1 -> 2 -> 4
    # 1 -> 3 -> 4
    a = ListNode(-10)
    b = ListNode(-10)
    c = ListNode(-9)
    d = ListNode(4)
    e = ListNode(1)
    f = ListNode(6)
    h = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = h
    _e = ListNode(-7)
    #printNode(b)
    sln = Solution()
    m = ListNode(2)
    n = ListNode(1)
    printNode(sln.mergeTwoLists(m, n))

if __name__ == '__main__':
    main()
