import itertools

class Solution:
    def numberOfBoomerangs(self, points):
        if len(points) < 3:
            return 0
        count = 0
        ps = itertools.permutations(points, 3)
        for s in ps:
            if self.helper(s):
                count += 1
        return count

    def helper(self, points):
        p1, p2, p3 = points[0], points[1], points[2]
        d1 =  (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        d2 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
        return d1 == d2
def main():
    points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
    sln = Solution()
    print(sln.numberOfBoomerangs(points))

if __name__ == '__main__':
    main()
