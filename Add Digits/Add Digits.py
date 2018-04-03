class Solution:
    def addDigits(self, num):
        if num < 10:
            return num
        return self.addDigits(sum(self.splitDigits(num)))

    def splitDigits(self, num):
        result = []
        while num >= 10:
            result.append(num%10)
            num = num // 10
        result.append(num)
        return result
def main():
    sln = Solution()
    print(sln.addDigits(10))

if __name__ == '__main__':
    main()
