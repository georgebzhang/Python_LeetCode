from bisect import bisect_right as bsr


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        N = len(nums)
        result = []
        for i in range(N-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, N-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, N-1
                while l < r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l = bsr(nums, nums[l])

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        ans = self.fourSum(nums, target)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
