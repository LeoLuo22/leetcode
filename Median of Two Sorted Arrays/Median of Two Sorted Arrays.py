class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        _len = len(nums)
        if _len % 2 == 0:
            mid = _len // 2
            return (nums[mid-1] + nums[mid]) / 2
        else:
            return nums[_len//2] / 1

def main():
    sln = Solution()
    print(sln.findMedianSortedArrays([1, 3], [2]))

if __name__ == '__main__':
    main()
