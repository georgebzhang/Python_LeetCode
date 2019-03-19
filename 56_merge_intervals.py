class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        num_intervals = len(intervals)
        if num_intervals == 1:
            return intervals

        intervals.sort(key=lambda interval: interval.start)
        result = []
        temp = intervals[0]
        for i in range(1, num_intervals):
            if intervals[i].start <= temp.end:
                if intervals[i].end > temp.end:
                    temp.end = intervals[i].end
            else:
                result.append(temp)
                temp = intervals[i]

            if i == num_intervals - 1:
                result.append(temp)

        return result

    def print_answer(self, ans):
        print('[', end='')
        for i in range(len(ans)):
            interval = ans[i]
            print('[{}, {}]'.format(interval.start, interval.end), end='')
            if i != len(ans) - 1:
                print(', ', end='')
        print(']')

    def test(self):
        input = [[1, 3], [2, 6], [8, 10], [15, 18]]
        intervals = []
        for s, e in input:
            interval = Interval(s, e)
            intervals.append(interval)
        ans = self.merge(intervals)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
