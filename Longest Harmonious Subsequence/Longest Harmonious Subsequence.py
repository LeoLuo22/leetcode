from collections import Counter
class Solution:
    def findLHS(self, nums):
        cs = Counter(nums)
        ans = 0
        for k in cs:
            if k + 1 in cs:
                ans = max(ans, cs[k]+cs[k+1])
        return ans

def main():
    sln = Solution()
    print(sln.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))

if __name__ == '__main__':
    main()
