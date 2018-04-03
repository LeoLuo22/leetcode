class Solution:
    def selfDividingNumbers(self, left, right):
        results = []
        for i in range(left, right+1):
            if self.isSelfDividing(i):
                results.append(i)
        return results
    def isSelfDividing(self, num):
        nums = str(num)
        for n in nums:
            n = int(n)
            if n == 0:
                return False
            if num % n != 0:
                return False
        return True

def main():
    solution = Solution()
    print(solution.selfDividingNumbers(1, 22))

if __name__ == '__main__':
    main()
