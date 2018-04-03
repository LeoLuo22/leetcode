class Solution:
    def isPowerOfThree(self, num):
        if num == 1:
            return True
        if abs(num) < 3 or num % 3 != 0:
            return False
        return self.isPowerOfThree(num//3)

def main():
    sln = Solution()
    print(sln.isPowerOfThree(9))

if __name__ == '__main__':
    main()
