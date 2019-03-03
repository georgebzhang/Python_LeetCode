class Solution(object):
    def print_mem(self, mem):
        for i in range(len(mem)):
            for j in range(len(mem[0])):
                print(mem[i][j], " ", end="")
            print()

    def longestPalindrome(self, s):  # O(n^2)
        n = len(s)

        mem = [[False] * n for i in range(n)]
        max_length = 1
        begin_index = 0

        for i in range(n):  # length 1 substrings
            mem[i][i] = True

        for i in range(n - 1):  # length 2 substrings
            if s[i + 1] == s[i]:
                max_length = 2
                begin_index = i
                mem[i][i + 1] = True

        for curr_length in range(3, n + 1):  # length 3+ substrings
            for i in range(n - curr_length + 1):
                j = i + curr_length - 1
                if s[i] == s[j] and mem[i + 1][j - 1] is True:
                    begin_index = i
                    max_length = curr_length
                    mem[i][j] = True

        return s[begin_index:begin_index + max_length]

    def print_answer(self, ans):
        print(ans)

    def test(self):
        s = 'babad'
        ans = self.longestPalindrome(s)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
