class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [None] * (4 * n)

        def leaf(v):
            v %= k
            c = [0] * k
            c[v] = 1
            return v, c

        def merge(a, b):
            if not a: return b
            if not b: return a

            p1, c1 = a
            p2, c2 = b
            p = (p1 * p2) % k
            c = c1[:]

            for r in range(k):
                c[(p1 * r) % k] += c2[r]

            return p, c

        def build(i, l, r):
            if l == r:
                tree[i] = leaf(nums[l])
                return
            m = (l + r) // 2
            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def update(i, l, r, pos, v):
            if l == r:
                tree[i] = leaf(v)
                return
            m = (l + r) // 2
            if pos <= m:
                update(i * 2, l, m, pos, v)
            else:
                update(i * 2 + 1, m + 1, r, pos, v)
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def query(i, l, r, ql, qr):
            if qr < l or r < ql:
                return None
            if ql <= l and r <= qr:
                return tree[i]
            m = (l + r) // 2
            return merge(
                query(i * 2, l, m, ql, qr),
                query(i * 2 + 1, m + 1, r, ql, qr)
            )

        build(1, 0, n - 1)

        ans = []
        for idx, val, start, x in queries:
            nums[idx] = val
            update(1, 0, n - 1, idx, val)
            ans.append(query(1, 0, n - 1, start, n - 1)[1][x])

        return ans