from datastructure import ListNode

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return
        arrayA = ListNode.toArray(headA)
        arrayB = ListNode.toArray(headB)
        lenA = len(arrayA)
        lenB = len(arrayB)
        if lenA >= lenB:
            big = arrayA
            small = arrayB
        else:
            big  = arrayB
            small = arrayA
        div = abs(lenA-lenB)
        loop = min(len(arrayA), len(arrayB))-1
        index = loop

        for i in range(loop, -1, -1):
            if small[i] == big[i+div]:
                index -= 1
            else:
                break

        array = small[index+1: len(small)]
        return ListNode.toList(array)

def main():
    a = ListNode.toList([1, 2])
    b = ListNode.toList([1, 2])
    headA = ListNode.toList(['a1', 'a2', 'c1', 'c2', 'c3'])
    headB = ListNode.toList(['b1', 'b2', 'b3', 'c1', 'c2', 'c3'])
    sln = Solution()
    sln.getIntersectionNode(headB, headA).show()

if __name__ == '__main__':
    main()
