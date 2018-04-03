class Solution:
    def addStrings(self, num1, num2):
        nums1 = list(num1)
        len1 = len(nums1)
        nums2 = list(num2)
        len2 = len(nums2)
        n1, n2 = 0, 0
        for i in range(len1):
            digit = int(nums1[i])
            n1 += digit * 10 ** (len1-i-1)
        for j in range(len2):
            n2 += int(num2[j]) * 10 ** (len2-j-1)
        return int(n1 + n2)

def main():
    sln = Solution()
    print(sln.addStrings('110', '20'))

if __name__ == '__main__':
    main()
