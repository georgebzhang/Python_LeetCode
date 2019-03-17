from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        l = [(v, k) for k, v in c.items()]

        l_k = l[:k]
        heapq.heapify(l_k)

        for i in range(k, len(l)):
            if l[i][0] > l_k[0][0]:
                heapq.heappop(l_k)
                heapq.heappush(l_k, l[i])

        # result = [vk[1] for vk in l_k]  # if don't care about order of results

        result = []
        for i in range(k):
            result.append(heapq.heappop(l_k)[1])

        return result[::-1]

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
