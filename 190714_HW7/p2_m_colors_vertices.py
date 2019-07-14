def check_neighbor_color(v, graph, colors, c):
    for i in range(len(graph[0])):
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True


def helper(graph, m, colors, vertices_count, cur_vertex):
    if cur_vertex == vertices_count:
        return True
    for c in range(m):
        if check_neighbor_color(cur_vertex, graph, colors, c):
            colors[cur_vertex] = c
            if helper(graph, m, colors, vertices_count, cur_vertex + 1):
                return True
            colors[cur_vertex] = -1
    return False


def color(graph, m):
    vertices_count = len(graph[0])
    colors = [-1 for _ in range(vertices_count)]
    colors[0] = 0
    return helper(graph, m, colors, vertices_count, 1)


if __name__ == '__main__':
    m = 3
    g = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
    print(color(g, m))
