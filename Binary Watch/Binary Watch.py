class Solution:
    def readBinaryWatch(self, num):
        results = []
        for i in range(12):
            h = bin(i).count('1')
            for j in range(60):
                m = bin(j).count('1')
                if m + h == num:
                    results.append('%d:%02d'%(i, j))

        return results



def main():
    sln = Solution()
    print(sln.readBinaryWatch(1))

if __name__ == '__main__':
    main()
