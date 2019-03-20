class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def canAttendMeetings(self, intervals):
        result = True
        intervals.sort(key=lambda interval: interval.start)
        prev_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start < prev_interval.end:
                result = False
        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        input = [[0, 30], [5, 10], [15, 20]]
        intervals = []
        for s, e in input:
            interval = Interval(s, e)
            intervals.append(interval)
        ans = self.canAttendMeetings(intervals)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
