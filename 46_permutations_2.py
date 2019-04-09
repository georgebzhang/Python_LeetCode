class Solution(object):
    def permute(self, nums):
        n = len(nums)
        if n < 2:
            return [nums]
        n1, n2 = nums[0], nums[1]
        result = [[n1, n2], [n2, n1]]
        for i in range(2, n):
            temp = []
            while result:
                perm = result.pop()
                for j in range(len(perm)+1):
                    copy = perm.copy()
                    copy.insert(j, nums[i])
                    temp.append(copy)
            result = temp
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
