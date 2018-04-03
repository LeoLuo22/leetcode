class Solution:
    def letterCasePermutation(self, S):
        from itertools import combinations
        r = list(S)
        for i in range(len(S)):
            if S[i].isalpha():
                r.append()


def main():
    S = 'a1b2'
    sln = Solution()
    print(sln.letterCasePermutation(S))

if __name__ == '__main__':
    main()
