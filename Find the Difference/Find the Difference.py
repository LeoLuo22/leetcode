class Solution:
    def findTheDifference(self, s, t):
        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()
        for i in range(len(list_t)):
            try:
                if list_t[i] != list_s[i]:
                    return list_t[i]
            except:
                return list_t[len(list_t)-1]



def main():
    sln = Solution()
    print(sln.findTheDifference('abcd', 'abcde'))

if __name__ == '__main__':
    main()
