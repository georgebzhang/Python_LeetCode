from collections import deque


class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        result = 0
        e_dict = {}
        for e in employees:
            e_dict[e.id] = e

        q = deque([id])
        while q:
            curr_id = q.popleft()
            result += e_dict[curr_id].importance
            q.extend(e_dict[curr_id].subordinates)

        return result

    def print_ans(self, ans):
        print(ans)

    def build_employees_list(self, vals):
        employees = []
        for val in vals:
            employees.append(Employee(val[0], val[1], val[2]))
        return employees

    def test(self):
        vals = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
        id = 1
        employees = self.build_employees_list(vals)
        ans = self.getImportance(employees, id)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
