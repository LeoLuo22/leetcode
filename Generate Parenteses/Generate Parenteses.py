from itertools import permutations
class Solution:
    def generateParenthesis(self, n):
        pars = ['(' for i in range(n)] + [')' for i in range(n)]
        coms = list(permutations(pars))
        print(coms)

def main():
    sln = Solution()
    print(sln.generateParenthesis(3))

if __name__ == '__main__':
    main()
