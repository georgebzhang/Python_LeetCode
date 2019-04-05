from bisect import bisect_left as bsl, bisect_right as bsr


class Solution(object):
    def searchRange(self, nums, target):
        def ind_first(target):
            ind = bsl(nums, target)
            if ind != len(nums) and nums[ind] == target:
                return ind
            raise ValueError

        def ind_last(target):
            ind = bsr(nums, target)-1
            if ind != len(nums) and nums[ind] == target:
                return ind
            raise ValueError

        result = [-1, -1]

        try:
            result = [ind_first(target), ind_last(target)]
        except:
            pass

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        ans = self.searchRange(nums, target)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
