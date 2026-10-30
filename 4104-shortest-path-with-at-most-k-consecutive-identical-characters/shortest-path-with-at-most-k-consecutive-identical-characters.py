import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][count]
        INF = float('inf')
        dist = [[[INF] * (k + 1) for _ in range(26)] for _ in range(n)]

        # Starting node
        start_char = ord(labels[0]) - ord('a')
        dist[0][start_char][1] = 0

        pq = [(0, 0, start_char, 1)]

        while pq:
            cost, node, prev_char, count = heapq.heappop(pq)

            if cost != dist[node][prev_char][count]:
                continue

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:

                curr_char = ord(labels[nei]) - ord('a')

                if curr_char == prev_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][curr_char][new_count]:
                    dist[nei][curr_char][new_count] = new_cost

                    heapq.heappush(
                        pq,
                        (new_cost, nei, curr_char, new_count)
                    )

        return -1