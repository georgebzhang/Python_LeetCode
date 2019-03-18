def top_sort(graph):
    result = []  # acts as a stack if using dependencies with edges directed from vertices to neighbors
    visited = set()

    def dfs(vertex):
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

        result.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    # result.reverse()
    return result


if __name__ == '__main__':
    # if using this dependencies, no result.reverse()
    dependencies = {  # vertex: [neighbors], edge directed from neighbors to vertex
        0: [],
        1: [0],
        2: [0],
        3: [1, 2],
        4: [3]
    }

    # if using this dependencies, use result.reverse()
    # dependencies = {  # vertex: [neighbors], edge directed from vertex to neighbors
    #     0: [1, 2],
    #     1: [3],
    #     2: [3],
    #     3: [4],
    #     4: [0]
    # }

    print(top_sort(dependencies))
