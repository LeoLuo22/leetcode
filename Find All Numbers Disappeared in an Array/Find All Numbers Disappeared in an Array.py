class Solution:
    def findDsiappearedNumber(self, nums):
        _len = len(nums)
        result = []
        for i in range(1, _len+1):
            if i not in nums:
                result.append(i)
        return result

def main():
    sln = Solution()
    print(sln.findDsiappearedNumber([4, 3, 2, 7, 8, 2, 3, 1]))

if __name__ == '__main__':
    main()
