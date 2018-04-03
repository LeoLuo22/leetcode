class Solution:
    def strStr(self, haystack, needle):
        if haystack == needle:
            return 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        for i in range(haystack_len):
            if haystack[i:needle_len+i] == needle:
                return i
        return -1

def main():
    sln = Solution()
    print(sln.strStr('', ''))

if __name__ == '__main__':
    main()
