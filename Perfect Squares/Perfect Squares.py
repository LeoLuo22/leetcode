import math
class Solution:

    def numSquares(self, n):
        for i in range(n, 1, -1):
            if self.isSquare(i):


    def isSquare(self, n):
        n = math.sqrt(n)
        return int(n) == n

def main():
    sln = Solution()
    print(sln.isSquare(4))
    print(sln.numSquares(12))

if __name__ == '__main__':
    main()
