
class Solution:
    def romanToInt(self, s):
        mapping = {'V': 5, 'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'D': 500, 'L': 50}
        nums = []
        for i in range(len(s)):
            nums.append(mapping.get(s[i]))
        total = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                total += nums[i]
            else:
                total -= nums[i]
        total += nums[len(nums)-1]
        return total
        print(nums)

def main():
    xs = [1, 2, 3]
    print(list(reduce(lambda x: x+1, xs)))

if __name__ == '__main__':
    main()
