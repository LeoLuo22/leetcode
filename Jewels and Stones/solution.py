class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        for s in S:
            for j in J:
                if s == j:
                    count += 1
        return count

def main():
    solution = Solution()
    print(solution.numJewelsInStones("aA", "aAAbbbb"))

if __name__ == '__main__':
    main()
