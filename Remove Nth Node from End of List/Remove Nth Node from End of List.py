from datastructure import ListNode

class Solution:
    def removeNthFromEnd(self, head, n):
        nodes = ListNode.toArray(head)
        print(nodes)
        index = len(nodes) - n
        del nodes[index]
        if len(nodes) == 0:
            return
        return ListNode.toList(nodes)

def main():
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(7)
    # head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    sln = Solution()
    print(sln.removeNthFromEnd(head, 1).show())

if __name__ == '__main__':
    main()
