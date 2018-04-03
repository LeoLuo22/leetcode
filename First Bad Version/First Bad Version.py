class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left <= right:
            if left == right:
                return left
            mid = (left+right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1



def main():
    sln = Solution()
    print(sln.firstBadVersion(1))

if __name__ == '__main__':
    main()
