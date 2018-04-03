class Solution:
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

def main():
    sln = Solution()
    move = 'RLUURDDDLU'
    print(sln.judgeCircle(move))

if __name__ == '__main__':
    main()
