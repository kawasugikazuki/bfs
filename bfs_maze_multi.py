from collections import deque
H, W = [int(i) for i in input().split()]

S = [['*']*W for _  in range(H)]

entry = []

for i in range(H):
  s = [c for c in input()]
  for j, v in enumerate(s):
    S[i][j] = v
    if v == 'E':
      entry.append((i,j))

def bfs(starts, maze, height, width):
  dist = [['#']*W for _ in range(H)]
  movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  visited = [[False]*W for _ in range(H)]
  queue = deque()
  for sy, sx in starts:
    dist[sy][sx] = 'E'
    visited[sy][sx] = True
    queue.append((sx, sy))

  while queue:
    x, y = queue.popleft()

    for dx, dy in movements:
      nx, ny = x + dx, y + dy
      if 0 <= nx < width and 0 <= ny < height:
        if not visited[ny][nx] and S[ny][nx] != '#':
          if dx == 1:
            dist[ny][nx] = '<'
          elif dx == -1:
            dist[ny][nx] = '>'
          elif dy == 1:
            dist[ny][nx] = '^'
          else:
            dist[ny][nx] = 'v'
          queue.append((nx, ny))
          visited[ny][nx] = True

  return dist


dist = bfs(entry, S, H, W)

for i in range(H):
  for j in range(W):
    print(dist[i][j], end='')
  print()
