class Solution:
    def letterCasePermutation(self, S):
        results = []
        S = S.upper()
        for i in range(len(S)):
            if S[i].isalpha():
                results.append
