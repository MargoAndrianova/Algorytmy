import heapq

n = 0
graph = []

def init(vertices, edges):
    """
    Ініціалізація графа.
    Викликається один раз на початку виконання програми.
    :param vertices: кількість вершин графа
    :param edges: кількість ребер графа (не використовується напряму)
    """
    global n, graph
    n = vertices
    graph = [[] for _ in range(n+1)]


def addEdge(source, destination, weight):
    """
    Додає орієнтоване зважене ребро у граф.
    :param source: вершина, з якої виходить ребро
    :param destination: вершина, у яку входить ребро
    :param weight: вага ребра
    """
    graph[source].append((destination, weight))


def findDistance(start, end):
    """
    Знаходить довжину найкоротшого шляху між start та end
    у зваженому орієнтованому графі.
    Використовує алгоритм Дейкстри (усі ваги ≥ 0).
    :param start: початкова вершина
    :param end: кінцева вершина
    :return: мінімальна відстань або -1, якщо шляху немає
    """
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heap = [(0, start)]  # (поточна відстань, вершина)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == end:
            break
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist[end] if dist[end] != float('inf') else -1
