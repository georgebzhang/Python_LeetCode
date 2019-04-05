class Solution(object):
    def maxSubArray(self, nums):
        def maxSubArrayCross(i, m, j):
            left_sum = None
            curr_sum = 0
            for k in range(m, i-1, -1):
                curr_sum += nums[k]
                if not left_sum or curr_sum > left_sum:
                    left_sum = curr_sum

            right_sum = None
            curr_sum = 0
            for k in range(m+1, j+1):
                curr_sum += nums[k]
                if not right_sum or curr_sum > right_sum:
                    right_sum = curr_sum

            return left_sum+right_sum

        def maxSubArrayRec(i, j):
            if i == j:
                return nums[i]
            m = (i+j)//2
            left_sum = maxSubArrayRec(i, m)
            right_sum = maxSubArrayRec(m+1, j)
            cross_sum = maxSubArrayCross(i, m, j)
            return max(left_sum, right_sum, cross_sum)

        n = len(nums)
        return maxSubArrayRec(0, n-1)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        ans = self.maxSubArray(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
