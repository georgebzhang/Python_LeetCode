from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.count = OrderedDict()

    def __len__(self):
        return len(self.map)

    def get(self, key: int) -> int:
        try:
            self.count[key] += 1
            return self.map[key]
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            return
        if len(self) == self.capacity:
            # print(self.count)
            min_count = min(self.count.values())
            lru_key = None
            for k in self.count:
                if self.count[k] == min_count:
                    lru_key = k
            # print(lru_key)
            del self.map[lru_key]
            del self.count[lru_key]
        self.map[key] = value
        self.count[key] = 0


class Solution(object):
    def print_answer(self, ans):
        print(ans)

    def test(self):
        commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        commands_params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

        output = []
        answer = [None, None, None, 1, None, -1, None, -1, 3, 4]
        print(answer)

        obj = None
        if commands[0] == 'LRUCache':
            obj = LRUCache(*commands_params[0])
            output.append(None)
        else:
            raise Exception('LRUCache not initialized!')

        for i in range(1, len(commands)):
            command = commands[i]
            if command == 'put':
                output.append(obj.put(*commands_params[i]))
            elif command == 'get':
                output.append(obj.get(*commands_params[i]))
            else:
                raise Exception('Invalid command!')
        print(output)
        self.print_answer(output == answer)


if __name__ == '__main__':
    s = Solution()
    s.test()
