class Solution:
    def isPowerOfFour(self, num):
        if num == 1:
            return True
        if abs(num) < 4 or num % 4 != 0:
            return False
        return self.isPowerOfFour(num//4)

def main():
    sln = Solution()
    print(sln.isPowerOfFour(24))

if __name__ == '__main__':
    main()
