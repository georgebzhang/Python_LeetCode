# https://www.youtube.com/watch?v=fV-TF4OvZpk&t=140s
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/275369/Python-O(NlogN)-Greedy
from bisect import bisect_left as bsl


class Solution(object):
    def lengthOfLIS(self, nums):
        seq = []
        for num in nums:
            i = bsl(seq, num)
            if i == len(seq):
                seq.append(num)
            else:
                seq[i] = num

        return len(seq)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        ans = self.lengthOfLIS(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
