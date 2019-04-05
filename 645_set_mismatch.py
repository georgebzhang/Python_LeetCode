class Solution(object):
    def findErrorNums(self, nums):
        result = []
        n = len(nums)
        s = set()
        dup = None
        xor_sum = 1
        for i in range(2, n+1):
            xor_sum ^= i
        for num in nums:
            if num in s:
                dup = num
                continue
            s.add(num)
            xor_sum ^= num
        result.append(dup)
        result.append(xor_sum)
        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 2, 2, 4]
        ans = self.findErrorNums(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
