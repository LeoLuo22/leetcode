class Solution:
    def addBinary(self, a, b):
        r = []
        a = [int(_) for _ in list(a)]
        b = [int(_) for _ in list(b)]
        len_a = len(a)
        len_b = len(b)
        if len_a == len_b:
            big, small = a, b
        elif len_a > len_b:
            big = a
            small = b
            big.reverse()
        else:
            big = b
            small = a
            big.reverse()
        for i in range(len(big)-len(small)):
            small.append(0)

        for i in range(len(big)):
            tmp = small[i] + big[i]
            left = tmp % 2
            up = tmp // 2
            r.append(left)
            if up == 0:
                continue
            if i+1 >= len(big):
                r.append(up)
            else:
                small[i+1] += up
        r.reverse()
        r = [str(_) for _ in r]
        return ''.join(r)


def main():
    sln = Solution()
    print(sln.addBinary('1010', '1011'))

if __name__ == '__main__':
    main()
