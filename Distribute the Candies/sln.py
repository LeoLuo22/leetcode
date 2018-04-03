class Solution:
    def distributeCandies(self, candies):
        uniques = set(candies)
        max_kinds = len(candies) // 2
        uniques_len = len(uniques)
        return max_kinds if uniques_len >= max_kinds else uniques_len

def main():
    sln = Solution()
    print(sln.distributeCandies([1,1,2,3]))

if __name__ == '__main__':
    main()
