from itertools import combinations

class Solution:
    def threeSum(self, nums):
        coms = combinations(nums, 3)
        coms = [sorted(com) for com in coms]
        r = []
        for com in coms:
            if sum(com) == 0 and com not in r:
                r.append(com)
        return r


def main():
    sln = Solution()
    # -1 0 1
    # -1 -1 2
    print(sln.threeSum([-1, 0, 1, 2, -1, -4]))

if __name__ == '__main__':
    main()
