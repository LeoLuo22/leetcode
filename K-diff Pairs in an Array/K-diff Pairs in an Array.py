class Solution:
    def findPair(self, nums, k):
        from itertools import combinations
        coms = combinations(nums, 2)
        r = []
        for com in coms:
            if abs(com[0]-com[1]) == k:
                r.append(com)
        r = [tuple(sorted(_)) for _ in r]
        return len(set(r))

def main():
    a = [1, 3, 1, 5, 4]
    b = [1, 1, 1, 2, 1]
    sln = Solution()
    #print(sln.findPair(a, 0))
    print(sln.findPair(b, 1))

if __name__ == '__main__':
    main()
