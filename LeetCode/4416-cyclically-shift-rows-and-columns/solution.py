class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        t=[[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            k=rowShift[i]
            for j in range(n):
                nc=(j-k+n)%n
                t[i][nc]=grid[i][j]
        res=[[0 for j in range(n)] for i in range(n)]
        for j in range(n):
            k=colShift[j]
            for i in range(n):
                nr=(i-k+n)%n
                res[nr][j]=t[i][j]
        return res
