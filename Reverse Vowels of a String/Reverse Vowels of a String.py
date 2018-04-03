class Solution:
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U']
        positions = []
        for i in range(len(s)):
            tmp = []
            if s[i] in vowels:
                tmp.append(i)
                tmp.append(s[i])
                positions.append(tmp)

        start, end = 0, len(positions)-1
        s = list(s)
        while start < end:
            start_item = positions[start]
            end_item = positions[end]
            s[start_item[0]] = end_item[1]
            s[end_item[0]] = start_item[1]
            start += 1
            end -= 1
        return ''.join(s)

def main():
    sln = Solution()
    print(sln.reverseVowels('hello'))
    print(sln.reverseVowels('leetcode'))

if __name__ == '__main__':
    main()
