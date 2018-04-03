class Solution:
    def hammingWeight(self, n):
        return len(str(bin(n)).replace('0', ''))-1

def main():
    solution = Solution()
    print(solution.hammingWeight(1))

if __name__ == '__main__':
    main()
