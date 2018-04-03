class Solution:
    def rotate(self, nums, k):
        length = len(nums)
        if k < 0:
            return
        if k == 0 or k % length == 0:
            return
        while k >=  length:
            k = k - length
        nums = nums[length-k:length] + nums[0:length-k]
        print(nums)


def main():
    solution = Solution()
    a = solution.rotate([1], 0)
    print(a)

if __name__ == '__main__':
    main()
print('hello')
