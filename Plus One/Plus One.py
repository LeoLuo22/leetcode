class Solution:
    def plusOne(self, digits):
        return [i+1 for i in digits]

def main():
    sln = Solution()
    print(sln.plusOne([1, 2]))

if __name__ == '__main__':
    main()
