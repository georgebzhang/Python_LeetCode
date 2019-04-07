class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < m:
            nums.append(nums1[i])
            i += 1
        while j < n:
            nums.append(nums2[j])
            j += 1
        nums1[:] = nums

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
