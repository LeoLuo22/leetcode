from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magzine):
        ransomNotes = Counter(ransomNote)
        magzines = Counter(magzine)
        for k, v in ransomNotes.items():
            if not ms.get(k):
                return False
            if v <= magzines.get(k):
                continue
            else:
                return False
        return True
def main():
    sln = Solution()
    print(sln.canConstruct('fffbfg', 'effjfggbffjdgbjjhhedh'))

if __name__ == '__main__':
    main()
