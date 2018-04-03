class Solution:
    def isPalindrome(self, x):
        x = str(x)
        _len = len(x)
        for i in range(len(x)):
            if x[i] != x[_len-1-i]:
                return False
        return True

def main():
    sln = Solution()
    print(sln.isPalindrome(123321))

if __name__ == '__main__':
    main()
