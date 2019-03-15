from collections import Counter


class Solution(object):
    def threeSum(self, nums):
        c = Counter(nums)

        # List out all the 3somes.
        threeSums = set()
        for key_1 in c:
            remainder = 0 - key_1
            for key_2 in c:
                key_3 = remainder - key_2
                if key_3 in c:
                    threeSums.add(tuple(sorted([key_1, key_2, key_3])))

        # Check that we aren't using any elements more times than they were in the original list.
        validThreeSums = []
        for triple in threeSums:
            a = Counter(triple)
            if all(a[key] <= c[key] for key in a):
                validThreeSums.append(triple)

        return list(validThreeSums)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [-1, 0, 1, 2, -1, -4]
        ans = self.threeSum(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
