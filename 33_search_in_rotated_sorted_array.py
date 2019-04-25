from bisect import bisect_left as bsl


class Solution:
    def search(self, nums, target):
        def rotation_index():
            l, r = 0, N-1
            if nums[l] < nums[r]:
                return 0

            while l <= r:
                m = (l+r)//2
                if nums[m] > nums[m+1]:
                    return m+1
                if nums[m] < nums[l]:
                    r = m-1
                else:  # assuming no duplicates in nums
                    l = m+1
            return -1

        def index(nums, target, lo=0, hi=len(nums)):
            ind = bsl(nums, target, lo, hi)
            if ind != len(nums) and nums[ind] == target:
                return ind
            return -1

        N = len(nums)
        if N == 0:
            return -1
        if N == 1:
            return index(nums, target)

        ind_rot = rotation_index()
        nums_search = None
        offset = None
        if ind_rot == 0:
            return index(nums, target)
        elif target < nums[0]:
            return index(nums, target, ind_rot, N)
        else:
            return index(nums, target, 0, ind_rot)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        ans = self.search(nums, target)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
