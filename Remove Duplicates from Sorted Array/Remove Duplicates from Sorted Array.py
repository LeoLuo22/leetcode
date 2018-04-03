class Solution:
    def removeDuplicate(self, nums):
        for num in nums:
            while nums.count(num) > 1:
                nums.remove(num)
        return nums

def main():
    sln = Solution()
    print(sln.removeDuplicate([1, 1, 2]))

if __name__ == '__main__':
    main()
