class Solution:
    def findComplement(self, num):
        result = 0
        mapping = {'1':'0', '0':'1'}
        num = bin(num).replace('0b', '')
        num = list(num)
        for i in range(len(num)):
            num[i] = mapping.get(num[i])
        count = 0
        for i in range(len(num)-1, -1, -1):
            result += int(num[i]) * (2 ** count)
            count += 1
        return result
def main():
    sln = Solution()
    print(sln.findComplement(2))

if __name__ == '__main__':
    main()
