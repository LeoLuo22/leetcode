class Solution:
    def findRestaurant(self, list1, list2):
        d = {}
        r = []
        for v1, index1 in enumerate(list1):
            for v2, index2 in enumerate(list2):
                if index1 == index2:
                    d[index1] = v1 + v2
                    break
        common = min(d.items(), key=lambda x: x[1])[1]
        for key, value in d.items():
            if value == common:
                r.append(key)
        return r

def main():
    sln = Solution()
    print(sln.findRestaurant(['Shogun', 'Ta', 'Burger King', 'KFC'], ['KFC', 'Burger King', 'Ta', 'Shogun']))

if __name__ == '__main__':
    main()
