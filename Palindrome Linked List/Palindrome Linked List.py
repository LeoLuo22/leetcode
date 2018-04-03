from datastructure import ListNode

class Solution:
    def isPalindrome(self, head):
        x = self.toArray(head)
        print(x)
        _len = len(x)
        for i in range(_len):
            if x[i] != x[_len-1-i]:
                return False
        return True

    def toString(self, node):
        r = ''
        while node.next:
            r += str(node.val)
            node = node.next
        r += str(node.val)
        return r

    def toArray(self, node):
        r = []
        while node.next:
            r.append(node.val)
            node = node.next
        r.append(node.val)
        return r
def main():
    sln = Solution()
    node1 = ListNode(-129)
    node2 = ListNode(-129)
    node1.next = node2
    print(sln.isPalindrome(node1))

if __name__ == '__main__':
    main()
