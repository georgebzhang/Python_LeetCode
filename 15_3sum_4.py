class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        N = len(nums)
        for i in range(N-2):
            if nums[i] > 0:
                break  # nums sorted, impossible for nums[i]+nums[l]+nums[r] == 0
            if i > 0 and nums[i] == nums[i-1]:
                continue  # prevent duplicates in result

            l, r = i+1, N-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [-1, 0, 1, 2, -1, -4]
        ans = self.threeSum(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
