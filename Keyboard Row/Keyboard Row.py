class Solution:
    def findWords(self, words):
        results = []
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

    def is_one_row(self, word):
        word = word.lower()
        words = list(word)
        for _ in words:


def main():
    sln = Solution()
    print(sln.findWords(['Hello', 'Alaska', 'Dad', 'Peace']))
    num
