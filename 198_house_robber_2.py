class Solution:
    # O(n) time
    # O(1) space
    def rob(self, nums):
        if not nums:
            return 0

        prev_max = 0  # f(-1)
        curr_max = 0  # f(0)
        for num in nums:
            temp = curr_max
            curr_max = max(num + prev_max, curr_max)  # f(k) = max[Ai + f(k-2), f(k-1)]
            prev_max = temp

        return curr_max

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [2, 7, 9, 3, 1]
        ans = self.rob(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
