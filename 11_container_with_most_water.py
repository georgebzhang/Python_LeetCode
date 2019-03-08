class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_area = 0
        while i <= j:
            area = min(height[i], height[j]) * (j - i)
            if max_area < area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area

    def print_answer(self, ans):
        print(ans)

    def test(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        ans = self.maxArea(height)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
