from collections import deque

def bfs(start, G, N, L, g_station):
  dist = [float('inf')] * N
  dist[start] = 0
  queue = deque()
  queue.append(start)

  while queue:
    idx = queue.popleft()

    if g_station[idx] == 1 and dist[idx] >0:
      dist[idx] = 0
      queue.append(idx)
      continue

    for nidx, cost in G[idx]:
      new_cost = dist[idx] + cost
      if new_cost < dist[nidx] and new_cost <= L:
        dist[nidx] = new_cost
        queue.append(nidx)
  return dist


N, M ,L = [int(i) for i in input().split()]
g_station = list(map(int,list(input().strip())))

# print(N, M, L)
# print(g_station)
graph = [[] for _ in range(N)]
for _ in range(M):
  u, v, d = [int(i) for i in input().split()]
  graph[u-1].append((v-1, d))
  graph[v-1].append((u-1, d))

dist_from_start = bfs(0, graph, N, L, g_station)

# print(dist_from_start)

# スタート地点0から行ける地点の個数の出力
print(sum(dist_from_start[i] <= L for i in range(N)))


