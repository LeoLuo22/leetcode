class Solution:
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
                continue
            if i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result

def main():
    sln = Solution()
    print(sln.fizzBuzz(0))

if __name__ == '__main__':
    main()
