class Solution(object):
    def permute(self, nums):
        def permute_rec(perm, rem):
            if not rem:
                result.append(perm.copy())
            for i in range(len(rem)):
                permute_rec(perm+[rem[i]], rem[:i]+rem[i+1:])

        result = []
        permute_rec([], nums)
        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [1, 2, 3]
        ans = self.permute(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
