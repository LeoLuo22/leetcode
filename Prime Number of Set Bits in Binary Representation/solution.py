class Solution:
    def countPrimeSetBits(self, L, R):
        count = 0
        for i in range(L, R+1):
            if self.isPrime(self.bits(i)):
                count += 1
        return count
    def bits(self, n):
        return len(str(bin(n)).replace('0', ''))-1

    def isPrime(self, n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
def main():
    solution = Solution()
    print(solution.countPrimeSetBits(842, 888))

if __name__ == '__main__':
    main()
