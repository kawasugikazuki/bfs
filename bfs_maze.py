from collections import deque

def bfs(start_x, start_y, maze, H, W):
  visited = [[False] * W for _ in range(H)]
  dist = [[-1] * W for _ in range(H)]
  dist[start_y][start_x] = 0
  movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]

  queue = deque()
  queue.append((start_x, start_y))
  visited[start_y][start_x] = True

  while queue:
    x, y = queue.popleft()

    for dx, dy in movement:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < W and 0 <= ny < H:
        if not visited[ny][nx] and maze[ny][nx] != '#':
          visited[ny][nx] = True
          dist[ny][nx] = dist[y][x] + 1
          queue.append((nx, ny))

  return dist[H-1][W-1]



H, W = map(int, input().split())
maze = [input().strip() for _ in range(H)]

print(bfs(0, 0, maze, H, W))

