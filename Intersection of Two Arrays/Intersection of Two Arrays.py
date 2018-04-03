class Solution:
    def intersection(self, num1, num2):
        result = []
        num1, num2 = list(set(num1)), list(set(num2))
        num1_len, num2_len = len(num1), len(num2)
        if num1_len < num2_len:
            for i in range(num1_len):
                for j in range(num2_len):
                    if num1[i] == num2[j]:
                        result.append(num1[i])
                        break
        else:
            for i in range(num2_len):
                for j in range(num1_len):
                    if num2[i] == num1[j]:
                        result.append(num2[i])
                        break
        return result

def main():
    sln = Solution()
    print(sln.intersection([1, 2, 2, 1], [2, 2, 1]))

if __name__ == '__main__':
    main()
