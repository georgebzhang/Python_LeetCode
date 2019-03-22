from collections import Counter
from heapq import heapify, heappop, heappush, nsmallest


class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        return nsmallest(k, c, key=lambda num:-c[num])

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        ans = self.topKFrequent(nums, k)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
