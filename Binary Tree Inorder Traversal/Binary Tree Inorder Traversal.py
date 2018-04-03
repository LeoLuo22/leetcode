from datastructure import TreeNode

class Solution:
    def __init__(self):
        self.r = []
    def inorderTraversal(self, root):
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.r.append(root.val)
        self.inorderTraversal(root.right)
        return self.r
def main():
    sln = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    print(sln.inorderTraversal(a))

if __name__ == '__main__':
    main()
