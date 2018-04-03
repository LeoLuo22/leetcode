class Solution:
    def isUgly(self, num):
        if num == 1:
            return True
        elif num == 0:
            return False

        if num % 2 == 0:
            return self.isUgly(num // 2)
        elif num % 3 == 0:
            return self.isUgly(num // 3)
        elif num % 5 == 0:
            return self.isUgly(num // 5)
        return False

    def isPrime(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
            i = i ** 2
        return True
def main():
    sln = Solution()
    print(sln.isUgly(6))

if __name__ == '__main__':
    main()
