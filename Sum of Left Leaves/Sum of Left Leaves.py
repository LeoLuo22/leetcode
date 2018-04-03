class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        vals = []
        if not root:
            return 0
        left_root = root.left
        if left_root:
            while left_root.left:
                left_root = left_root.left
            if not left_root.right:
                vals.append(left_root.val)
        right_root = root.right
        flag = True
        if right_root:
            while flag:
                right_root = right_root.left
                if not right_root:
                    flag = False
                    break
                if not right_root.left and not right_root.right:
                    break
            if flag:
                vals.append(right_root.val)
        return sum(vals)

    def is_left_leaf(self, node):
        if node.left:
            node = node.left
            if not node.left and not node.right:
                return node.val
        return



def main():
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)
    e = TreeNode(10)
    """
    root.left = a
    a.right = e
    root.right = b
    b.left = c
    b.right = d
    """
    root.right = a
    sln = Solution()
    print(sln.sumOfLeftLeaves(root))

if __name__ == '__main__':
    main()
