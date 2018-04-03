class Solution:
    def longestCommonPrefix(self, strs):
        length = len(strs)
        if length == 0:
            return ""
        minSize = 100
        minIndex = 0
        for i in range(len(strs)):
            _len = len(strs[i])
            if _len == 0:
                return ''
            if _len < minSize:
                minSize = _len
                minIndex = i

        while True:
            count = 0
            for i in range(len(strs)):
                if strs[i][0:minSize] == strs[minIndex][0:minSize]:
                    count += 1
            if count == len(strs) or minSize <= 0:
                break
            else:
                minSize -= 1

        if minSize <= 0:
            return ""
        return strs[minIndex][0:minSize]

def main():
    sln = Solution()
    print(sln.longestCommonPrefix(["a", "b"]))

if __name__ == '__main__':
    main()
