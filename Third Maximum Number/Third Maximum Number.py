class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[2]

def main():
    sln = Solution()
    print(sln.thirdMax([2, 3, 2, 1]))

if __name__ == '__main__':
    main()
