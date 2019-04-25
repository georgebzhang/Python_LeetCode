from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        mapping = defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')] += 1

            mapping[tuple(key)].append(s)

        return list(mapping.values())

    def print_answer(self, ans):
        print(ans)

    def test(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        ans = self.groupAnagrams(strs)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
