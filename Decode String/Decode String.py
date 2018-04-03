class Solution:
    def decodeString(self, s):
        s = list(s)
        ops = []
        nums = []
        for _ in s:
            if _ == '[':
                ops.append(_)
            elif _ == ']':
                n = nums[-1]
                o = nums[-2]
                del nums[-1]
                del nums[-1]
                tmp = ''
                for i in range(0, int(o)):
                    tmp += n
                nums.append(tmp)
                print(nums)
                del ops[len(ops) - 1]
            else:
                nums.append(_)
        print(ops)
        print(nums)


def main():
    sln = Solution()
    print(sln.decodeString('3[a]2[bc]'))

if __name__ == '__main__':
    main()
