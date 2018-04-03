class Solution:
    def convertToBase7(self, num):
        r = ''
        n = abs(num)
        while n >= 7:
            r += str(n % 7)
            n = n // 7
        r += str(n)
        r = ''.join(reversed(r))
        return '-'+r if num < 0 else r

def main():
    sln = Solution()
    print(sln.convertToBase7(777)) # 202

if __name__ == '__main__':
    main()
