class Solution:
    def isValid(self, s):
        mapping = {'{':'}', '(':')', '[': ']'}
        stack = []
        s = list(s)
        for _ in s:
            if len(stack) == 0:
                stack.append(_)
                continue
            if _ in mapping.keys():
                stack.append(_)
            else:
                if mapping.get(stack[len(stack)-1]) == _:
                    stack.pop(len(stack)-1)
                else:
                    stack.append(_)
        return True if len(stack) == 0 else False

def main():
    sln = Solution()
    print(sln.isValid(']'))

if __name__ == '__main__':
    main()
