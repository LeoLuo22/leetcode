from datastructure import ListNode

class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return
        array = ListNode.toArray(head)
        if len(array) == 0:
            return
        r = []
        _len = len(array)
        for i in range(0, _len, k):
            if i + k > _len:
                r += array[i: _len]
                break
            tmp = array[i:k+i]
            tmp.reverse()
            r += tmp
        return ListNode.toList(r)

def main():
    array = [1, 2]
    head = ListNode.toList(array)
    sln = Solution()
    print(sln.reverseKGroup(head, 2).show())

if __name__ == '__main__':
    main()
