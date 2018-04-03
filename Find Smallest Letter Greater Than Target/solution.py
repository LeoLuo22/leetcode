class Solution:
    def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

def main():
    solution = Solution()
    print(solution.nextGreatestLetter(['c', 'f', 'g'], 'a'))

if __name__ == '__main__':
    main()
