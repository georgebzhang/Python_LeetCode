import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        nums_k = nums[:k]
        heapq.heapify(nums_k)
        for i in range(k, len(nums)):
            heapq.heappushpop(nums_k, nums[i])

        result = None
        result = heapq.heappop(nums_k)
        return result


    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        ans = self.findKthLargest(nums, k)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
