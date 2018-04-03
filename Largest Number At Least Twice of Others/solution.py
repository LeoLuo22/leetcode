class Solution:
    def dominantIndex(self, nums):
        max_value = nums[0]
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
                max_index = i
        for j in range(len(nums)):
            if j == max_index:
                continue
            if max_value < nums[j] * 2:
                return -1
        return max_index

def main():
    solution = Solution()
    print(solution.dominantIndex([1,2,3,4]))

if __name__ == '__main__':
    main()
