class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        lcp = ''
        ind = 0

        while True:
            letters = []

            for item in strs:
                if ind == len(item):
                    return lcp
                letters.append(item[ind])

            letter = set(letters)
            if len(letter) == 1:
                lcp += letter.pop()
            else:
                return lcp

            ind += 1

        return lcp

    def print_answer(self, ans):
        print(ans)

    def test(self):
        strs = ["flower", "flow", "flight"]
        ans = self.longestCommonPrefix(strs)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
