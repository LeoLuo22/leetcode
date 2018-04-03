from datastructure import ListNode
class Solution:
    def reverseBetween(self, head, m, n):
        array = head.toArray(head)
        array[m-1: n] = list(reversed(array[m-1: n]))
        return head.toList(array)

def main():
    sln = Solution()
    array = [1, 2, 3, 4, 5]
    node = ListNode(1)
    head = node.toList(array)
    print(sln.reverseBetween(head, 2, 4).show())

if __name__ == '__main__':
    main()
