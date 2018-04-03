class Solution:
    def findRelativeRanks(self, nums):
        _len = len(nums)
        mapping = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}
        sorted_nums = sorted(nums, reverse=True)
        results = [0 for i in range(_len)]
        for i in range(len(sorted_nums)):
            for j in range(len(nums)):
                if sorted_nums[i] == nums[j]:
                    if i <= 2:
                        results[j] = mapping.get(i)
                    else:
                        results[j] = str(i+1)
                    continue
        return results

def main():
    sln = Solution()
    print(sln.findRelativeRanks([5, 4, 3, 2, 1]))
    # Gold Medal Silver Medal Bronze Medal 4, 5

if __name__ == '__main__':
    main()
