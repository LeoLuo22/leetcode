class Solution:
    def getSum(self, a, b):
        a = bin(a)
        print(a)
        b = bin(b)
        print(a)
        print(type(a))
        print(a^b)

def main():
    sln = Solution()
    print(sln.getSum(2000, 3))

if __name__ == '__main__':
    main()
