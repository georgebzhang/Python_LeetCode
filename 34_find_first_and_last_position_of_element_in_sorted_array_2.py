class Solution(object):
    def searchRange(self, nums, target):
        def bs(target, first):  # first (boolean) indicates whether to return first or last occurence
            i = -1
            l, r = 0, len(nums)-1
            while l <= r:
                m = (l+r)//2
                if target == nums[m]:
                    i = m
                    if first:
                        r = m-1
                    else:
                        l = m+1
                elif target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            return i

        def ind_first(target):
            return bs(target, True)

        def ind_last(target):
            return bs(target, False)

        return [ind_first(target), ind_last(target)]

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
