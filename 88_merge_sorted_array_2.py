class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if not n:
            return
        i, j = m-1, n-1
        ind = m+n-1
        while j >= 0:
            if i < 0 or nums2[j] > nums1[i]:
                nums1[ind] = nums2[j]
                j -= 1
            else:
                nums1[ind] = nums1[i]
                i -= 1
            ind -= 1

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.merge(nums1, m, nums2, n)
        self.print_answer(nums1)


if __name__ == '__main__':
    s = Solution()
    s.test()
