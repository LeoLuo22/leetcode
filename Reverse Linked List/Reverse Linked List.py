from datastructure import ListNode

class Solution:
    def reverseList(self, head):
        array = self.toArray(head)
        return self.toList(list(reversed(array)))

    def toList(self, array):
        # 将数组转换为链表
        if len(array) == 0:
            return
        nodes = [ListNode(a) for a in array]
        cur = nodes[0]
        for i in range(1, len(nodes)):
            cur.next = nodes[i]
            cur = nodes[i]
        return nodes[0]

    def toArray(self, node):
        r = []
        while node.next:
            r.append(node.val)
            node = node.next
        r.append(node.val)
        return r

def main():
    sln = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    print(sln.reverseList(node1).show())

if __name__ == '__main__':
    main()
