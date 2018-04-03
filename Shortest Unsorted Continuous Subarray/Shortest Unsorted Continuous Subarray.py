class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        start, end = 0, 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i

        for j in range(len(nums)-1, -1, -1):
            if nums[j] != sorted_nums[j]:
                end = j
        if start != end:
            return abs(end - start) + 1
        return 0

def main():
    sln = Solution()
    # [2, 4, 6, 8, 9, 10, 15]
    # [2, 6, 4, 8, 10, 9, 15]
    print(sln.findUnsortedSubarray([2,6,4,8,10,9,15])) #output 5
    print(sln.findUnsortedSubarray([1, 2, 3, 4]))

if __name__ == '__main__':
    main()
