class Solution:
    def nthUglyNumber(self, n):
        uglies = [1]
        i2, i3, i5 = 0, 0, 0 # 索引
        while len(uglies) != n:
            u2, u3, u5 = 2 * uglies[i2], 3 * uglies[i3], 5 * uglies[i5]
            value = min(u2, u3, u5)
            uglies.append(value)
            if value == u2:
                i2 += 1
            if value == u3:
                i3 += 1
            if value == u5:
                i5 += 1
        print(uglies)
        return uglies[-1]
def main():
    sln = Solution()
    print(sln.nthUglyNumber(261))

if __name__ == '__main__':
    main()
