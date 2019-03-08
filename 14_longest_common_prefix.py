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

            letter = set(letters)  # convert list to set
            if len(letter) == 1:  # only 1 element in set if all items in list were same
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
