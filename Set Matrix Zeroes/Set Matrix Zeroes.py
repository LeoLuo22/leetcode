class Solution:
    def setZeros(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        indexes = []
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    indexes.append([i, j])
        for index in indexes:
            matrix[index[0]] = [0 for i in range(len(matrix[i]))]
            for i in range(row):
                matrix[i][index[1]] = 0
        print(matrix)
        print(indexes)


def main():
    sln = Solution()
    matrix = [ [1, 2, 3],
               [4, 5, 0]
             ]
    sln.setZeros(matrix)
    #print(matrix)

if __name__ == '__main__':
    main()

