class Solution:
    def searchInsert(self, nums, target):
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                return i

def main():
    sln = Solution()
    print(sln.searchInsert([1, 3, 5, 6], 0))

if __name__ == '__main__':
    main()
