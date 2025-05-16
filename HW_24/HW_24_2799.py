from collections import deque

def read():
    m, n, i, j = map(int, input().split())
    lab = []
    for _ in range(m):
        lab.append(list(input().rstrip()))
