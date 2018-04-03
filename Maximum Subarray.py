class Solution:
    def maxSubArray(self, nums):
        maxValue = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):



def main():
    sln = Solution()
    print(sln.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

if __name__ == '__main__':
    main()
