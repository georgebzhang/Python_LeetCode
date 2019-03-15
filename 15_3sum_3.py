from collections import Counter


class Solution(object):
    def threeSum(self, nums):
        c = Counter(nums)
        s = set()
        result = []
        for k1 in c:
            for k2 in c:
                k3 = 0 - k1 - k2
                if k3 in c:
                    s.add(tuple(sorted([k1, k2, k3])))

        for l in s:
            c1 = Counter(l)
            if all(c1[k] <= c[k] for k in c1):
                result.append(l)

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [-1, 0, 1, 2, -1, -4]
        ans = self.threeSum(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
