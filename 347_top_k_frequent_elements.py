from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        l = [(-v, k) for k, v in c.items()]
        heapq.heapify(l)
        l_k = []
        for i in range(k):
            l_k.append(heapq.heappop(l))

        result = [vk[1] for vk in l_k]
        return result

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
