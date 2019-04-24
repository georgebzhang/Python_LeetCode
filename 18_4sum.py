from collections import Counter


class Solution:
    def fourSum(self, nums, target):
        quads = set()
        c = Counter(nums)
        for k1 in c:
            for k2 in c:
                for k3 in c:
                    k4 = target-k1-k2-k3
                    if k4 in c:
                        quads.add(tuple(sorted([k1, k2, k3, k4])))

        result = []
        for quad in quads:
            c1 = Counter(quad)
            if all(c1[k] <= c[k] for k in c1):
                result.append(list(quad))
                
        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        ans = self.fourSum(nums, target)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
