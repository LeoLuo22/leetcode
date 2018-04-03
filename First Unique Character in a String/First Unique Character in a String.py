class Solution:
    def firstUniqChar(self, s):
        index = -1
        s = list(s)
        if len(s) == 2:
            if s[0] != s[1]:
                return 0
            else:
                return -1
        for i in range(len(s)):
            count = 0
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    count += 1
            if len(s) - i - 1 == count:
                index = i
                return index
        return index


def main():
    sln = Solution()
    print(sln.firstUniqChar('cc'))

if __name__ == '__main__':
    main()
