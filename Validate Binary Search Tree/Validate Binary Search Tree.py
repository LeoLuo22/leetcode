from datastructure import TreeNode

class Solution:
    def isValidBST(self, root):
        left = root.left
        right = root.right
        if left.val < root.val and right.val > root.val:
            return True

def main():
    sln = Solution()
    root = TreeNode(2)
    a  =TreeNode(1)
    b = TreeNode(3)
    root.left = a
    root.right = b
    print(sln.isValidBST(root))

if __name__ == '__main__':
    main()
