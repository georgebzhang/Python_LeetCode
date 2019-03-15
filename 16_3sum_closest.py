class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum == target:
                    return result
                elif sum < target:
                    j += 1
                else:
                    k -= 1

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [-1, 2, 1, -4]
        target = 1
        ans = self.threeSumClosest(nums, target)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
