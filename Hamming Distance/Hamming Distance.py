class Solution:
    def hammingDistance(self, x, y):
        count = 0
        base = '000000000000000000000000000000'
        x = bin(x).replace('b', '')
        y = bin(y).replace('b', '')
        x = base[0:32-len(x)] + x
        y = base[0:32-len(y)] + y
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1

        return count

def main():
    sln = Solution()
    print(sln.hammingDistance(1, 4))

if __name__ == '__main__':
    main()
