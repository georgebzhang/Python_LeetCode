from collections import Counter


class Solution(object):
    def subsets(self, nums):
        def subsets_rec(perm, rem):
            if not rem:
                result.append(perm.copy())
                return
            subsets_rec(perm + [rem[0]], rem[1:])  # include element
            subsets_rec(perm, rem[1:])  # ignore element

        result = []
        subsets_rec([], nums)
        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [1, 2, 3]
        ans = self.subsets(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
