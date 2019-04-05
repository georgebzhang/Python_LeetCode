from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        for num in c1:
            if num in c2:
                result.extend([num] * min(c1[num], c2[num]))

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        ans = self.intersect(nums1, nums2)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
