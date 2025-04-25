class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number
        self.mAdjacentList = [[] for i in range(vertex_number+1)]

    def addEdge(self, source, destination, weight=1):
        self.mAdjacentList[source].append(destination)
        if not self.mIsOriented:
            self.mAdjacentList[destination].append(source)

    def vertex(self, u):
        return self.mAdjacentList[u]

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    g = Graph(vertex_number = n)

    for i in range(k):
        parts = input().split()
        cmd = parts[0]
        if cmd == '1':
            u, v = int(parts[1]), int(parts[2])
            g.addEdge(u, v)
        else:
            u = int(parts[1])
            print(*g.vertex(u))
