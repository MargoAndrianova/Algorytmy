def dfs(i, j):
    visited[i][j] = True
    cnt = 1
    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj]=='.':
            cnt += dfs(ni, nj)
    return cnt


if __name__ == '__main__':
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    x, y = map(int, input().split())
    x -= 1; y -= 1
    visited = [[False]*n for _ in range(n)]
    print(dfs(x, y))