class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        while self.next:
            print(str(self.val) + '->', end='')
            self = self.next
        print(self.val)

    def toString(self):
        r = ''
        while self.next:
            r += str(self.val)
            self = self.next
        r += str(self.val)
        return r

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

    @staticmethod
    def toArray(node):
        r = []
        while node.next:
            r.append(node.val)
            node = node.next
        r.append(node.val)
        return r

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

    @staticmethod
    def toList(array):
        # 将数组转换为链表
        if len(array) == 0:
            return
        nodes = [ListNode(a) for a in array]
        cur = nodes[0]
        for i in range(1, len(nodes)):
            cur.next = nodes[i]
            cur = nodes[i]
        return nodes[0]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def inorderByStack(root):
        # 通过栈实现中序遍历
        results = []
        if not root:
            return results
        stack = []
        while root or not len(stack) == 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            results.append(root.val)
            root = root.right
        return results

def tree1():
    A = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')
    D = TreeNode('D')
    E = TreeNode('E')
    F = TreeNode('F')
    G = TreeNode('G')
    H = TreeNode('H')
    K = TreeNode('K')
    A.left = B
    A.right = E
    B.right = C
    C.left = D

    E.right = F
    F.left = G
    G.left = H
    G.right = K
    return A

LDRs = []
def inorderTraversal(root):
    # 中序遍历
    if not root:
        return
    inorderTraversal(root.left)
    LDRs.append(root.val)
    inorderTraversal(root.right)


def testLDR():
    root = tree1()
    inorderTraversal(root)
    print(LDRs)

def main():
    testLDR()
    print(TreeNode.inorderByStack(tree1()))
if __name__ == '__main__':
    main()
