from collections import deque


class Solution(object):
    def letterCombinations(self, digits):
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = deque()

        if digits:
            result.append('')
            for i in range(len(digits)):
                while len(result[0]) == i:
                    temp = result.popleft()
                    for item in phone[digits[i]]:
                        result.append(temp + item)

        return list(result)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        digits = '23'
        ans = self.letterCombinations(digits)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
