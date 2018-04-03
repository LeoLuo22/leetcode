class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        m = []
        rs = []
        for n1 in nums1:
            for n2 in nums2:
                tmp = []
                tmp.append(n1)
                tmp.append(n2)
                m.append(tmp)
        if len(m) < k:
            k = len(m)
        sums = list(map(sum, m))
        d = {}
        for _ in enumerate(sums):
            d[_[0]] = _[1]
        s = sorted(d.items(), key=lambda x: x[1])
        for i in range(k):
            rs.append(m[s[i][0]])
        return rs

def main():
    m1 = [1, 1, 2]
    m2 = [1, 2, 3]
    m3 = []
    m4 = []
    # [1,2] [1, 4] [1, 6]
    sln = Solution()
    print(sln.kSmallestPairs(m3, m4, 10))

if __name__ == '__main__':
    main()
