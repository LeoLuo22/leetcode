class Solution:
    def isHappy(self, n):
        if n == 1 or n == 7:
            return True
        if n < 10:
            return False
        r = map(lambda x: x*x, self.split_num(n))
        return self.isHappy(sum(list(r)))

    def split_num(self, n):
        results = []
        while n >= 10:
            results.append(n%10)
            n = n // 10
        results.append(n)
        return results
def main():
    sln = Solution()
    print(sln.isHappy(49))

if __name__ == '__main__':
    main()
