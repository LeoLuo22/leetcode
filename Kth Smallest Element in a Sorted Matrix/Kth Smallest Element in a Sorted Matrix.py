class Solution:
    def kthSmallest(self, matrix, k):
        m = [x for j in matrix for x in j]
        m.sort()
        return m[k-1]

def main():
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]
             ]
    m1 = [[-5]]
    m2 = [[1,2],
          [1,3]]

    sln = Solution()
    print(sln.kthSmallest(m2, 4))

if __name__ == '__main__':
    main()
