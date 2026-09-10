class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0 ,0
            ls, lc = dfs(root.left)
            rs, rc = dfs(root.right)
            total = root.val + ls + rs
            count = 1 + lc + rs
            count = 1 + lc + rc
            if root.val == total // count:
                ans += 1
            return total,count 
        dfs(root)
        return ans

        