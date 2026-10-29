
class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)

        # Euler tour and binary lifting
        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n

        timer = 0
        stack = [(0, 0, 0)]
        visited = [False] * n
        visited[0] = True

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                pref[u] = (pref[p] if u != 0 else 0) ^ (1 << (ord(chars[u]) - 97))
                parent[0][u] = p

                for j in range(1, LOG):
                    parent[j][u] = parent[j - 1][parent[j - 1][u]]

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if not visited[v]:
                        visited[v] = True
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Fenwick tree: range updates, point queries
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def point(i):
            i += 1
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return res

        def update_node(u, old, new):
            delta = (1 << (ord(old) - 97)) ^ (1 << (ord(new) - 97))
            add(tin[u], delta)
            if tout[u] + 1 < n:
                add(tout[u] + 1, delta)

        def get_prefix(u):
            return pref[u] ^ point(tin[u])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            j = 0
            while diff:
                if diff & 1:
                    u = parent[j][u]
                diff >>= 1
                j += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        result = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new = parts[2]
                update_node(u, chars[u], new)
                chars[u] = new

            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)

                mask = get_prefix(u) ^ get_prefix(v) ^ (1 << (ord(chars[w]) - 97))

                result.append((mask & (mask - 1)) == 0)

        return result

