import heapq

n = 0
graph = []

def init(vertices, edges):
    """
    Ініціалізація графа.
    Викликається один раз перед додаванням ребер.
    :param vertices: кількість вершин графа
    :param edges: кількість ребер (не використовується напряму)
    """
    global n, graph
    n = vertices
    graph = [[] for _ in range(n+1)]


def addEdge(source, destination, weight):
    """
    Додає орієнтоване зважене ребро у граф.
    :param source: вершина, з якої виходить ребро
    :param destination: вершина, у яку входить ребро
    :param weight: вага ребра (припускаємо, що >= 0)
    """
    graph[source].append((destination, weight))


def getWay(start, end):
    """
    Знаходить один з найкоротших шляхів між start та end
    у направленому зваженому графі (без від'ємних ребер).
    Використовує алгоритм Дейкстри.
    :param start: початкова вершина (1..n)
    :param end: кінцева вершина (1..n)
    :return: список вершин шляху від start до end включно,
             або порожній список, якщо шляху немає.
    """
    dist = [float('inf')] * (n+1)
    prev = [None] * (n+1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d_u, u = heapq.heappop(heap)
        if d_u > dist[u]:
            continue
        if u == end:
            break
        for v, w in graph[u]:
            nd = d_u + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))

    if dist[end] == float('inf'):
        return []

    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path
