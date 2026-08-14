class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        M, N = len(s), len(p)

        def dfs(i, j):
            if j == N:
                return i == M
            
            match = i < M and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < N and p[j + 1] == "*":
                return (dfs(i, j + 2) or (match and dfs(i + 1, j)))
            
            if match: return dfs(i + 1, j + 1)
            return False
            
        

        return dfs(0, 0)
        