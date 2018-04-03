class Solution:
    def matrixReshape(self, nums, r, c):
        if len(nums) == 0 :
            return nums
        maxtrix_length = len(nums[0]) * len(nums)
        if r * c != maxtrix_length:
            return nums
        rows = []
        for num in nums:
            for n in num:
                rows.append(n)

        results = []
        index = 0
        for _r in range(r):
            tmp = []
            for _c in range(c):
                tmp.append(rows[index])
                index += 1
            results.append(tmp)
        return results


def main():
    sln = Solution()
    print(sln.matrixReshape([[1,2],[3,4]],4,1))

if __name__ == '__main__':
    main()
