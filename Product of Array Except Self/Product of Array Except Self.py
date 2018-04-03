class Solution:
    def productExceptSelf(self, nums):
        pro = 1
        results = []
        for num in nums:
            if num != 0:
                pro *= num
        for num in nums:

            results.append(pro//num)
        return [pro // num for num in nums]

def main():
    sln = Solution()
    print(sln.productExceptSelf([1, 0]))

if __name__ == '__main__':
    main()
