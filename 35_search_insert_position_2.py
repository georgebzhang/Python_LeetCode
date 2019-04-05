class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return l

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 3, 5, 6]
        target = 5
        ans = self.searchInsert(nums, target)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
